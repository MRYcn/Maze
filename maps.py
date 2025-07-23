import json, math
from straight import Straight
from start import Start
from end import End
from impasse import Impasse
from turn import Turn
from three import Three
from four import Four
from floor import Floor
from arrow import Arrow

#map loader and manager

class Map_Manager:
    def __init__(self,navigator):
        self.game=navigator.game
        self.RW=self.game.REF_WIDTH
        self.RH=self.game.REF_HEIGHT

        map5_dict={
            'start':[600,255],
            'end':[800,355],
            'impasse':[[600,255,0]],
            'straight':[[800,155,90],[900,255,0],[800,355,90]],
            'turn':[[700,155,90],[900,155,0],[700,355,180],[900,355,270]],
            'three':[[700,255,270]],
            'arrow':[[700,255,0,'red_turn',True]]
        }
        map5_gid=[
            ['箭头表示仅允许前',[1080,155]],
            ['进的方向，此要求',[1080,205]],
            ['仅对沿箭尾方向进',[1080,255]],
            ['入的情况有效。',[1065,305]]
        ]
        map5_dict['guidance']=map5_gid
        with open('map5.json','w') as f:
            json.dump(map5_dict,f)
            print('written')

        map_files=['map1.json','map2.json','map3.json','map4.json','map5.json']
        self.map_dicts=[]
        for file in map_files:
            with open(file,'r') as f:
                self.map_dicts.append(json.load(f))

        self.navigator=navigator
        self.st=0
        self.moving=False
        self.press_pos=False
        self.action=None
        self.map_sufs=[]
    
    def update(self):#st: game.st
        if not self.navigator.moving and self.navigator.press_pos:
            self.action=self.judge_action()
            if self.action==None:
                self.navigator.press_pos=False
                return
            self.navigator.moving=True
        elif not self.navigator.press_pos:
            return

        if self.navigator.moving:
            self.move(self.action,self.map_sufs)
            self.game.beginning=False
            self.navigator.ang=self.action
        if self.map_sufs[0].loc[0]%100 ==0 and (self.map_sufs[0].loc[1]-255)%100==0:
            self.navigator.press_pos=False
            self.navigator.moving=False
    
    def display(self):#st: game.st
        for el in self.map_sufs:
            el.display()

    def get_level_num(self):
        return 5

    def judge_action(self):
        ang=self.round_ang()
        action = None
        arrow=None
        for suf in self.map_sufs:
            if suf.__class__.__name__=='Arrow' and suf.loc in [(590,245),(590,265),(610,245),(610,265),(600,255)] and suf.ang==self.navigator.ang:
                arrow=suf
            if suf.loc == (600, 255):
                if suf.__class__.__name__=='Straight' and abs(suf.ang - ang+90) in [0, 180]:
                    action = ang
                elif suf.__class__.__name__=='Impasse' and suf.ang==ang:
                    action=ang
                elif suf.__class__.__name__=='Turn' and suf.ang in (ang-180,ang-270,ang+180,ang+90):
                    action=ang
                elif suf.__class__.__name__=='Three' and suf.ang not in (ang-90,ang+270):
                    action=ang
                elif suf.__class__.__name__=='Four':
                    action=ang
                elif suf.__class__.__name__=='Floor' and ang==self.navigator.ang:
                    action=ang
        if abs(self.navigator.ang-ang)==180:
            action=None
        elif arrow and 'straight' in arrow.type and action!=arrow.ang:
            action=None
        elif arrow and 'turn' in arrow.type:
            if arrow.flip and action not in (arrow.ang+90,arrow.ang-270):
                action=None
            elif not arrow.flip and action not in (arrow.ang-90,arrow.ang+270):
                action=None
        return action

    def move(self,action,map_sufs):
        if action==0:
            for el in map_sufs:
                el.loc=(el.loc[0]-10,el.loc[1])
        elif action==90:
            for el in map_sufs:
                el.loc=(el.loc[0],el.loc[1]+10)
        elif action==180:
            for el in map_sufs:
                el.loc=(el.loc[0]+10,el.loc[1])
        else:
            for el in map_sufs:
                el.loc=(el.loc[0],el.loc[1]-10)

    def round_ang(self):
        x, y = self.navigator.press_pos
        if self.game.w / self.game.h >= 2.19:
            x,y=x * self.RH / self.game.h,y * self.RH / self.game.h
        else:
            x,y=x * self.RW / self.game.w,y * self.RW / self.game.w
        dx,dy=x-600,255-y
        if dx == 0:
            if dy > 0:
                ang = 90
            else:
                ang = -90
        elif dx > 0:
            ang = math.degrees(math.atan(dy / dx))
        else:
            ang = math.degrees(math.atan(dy / dx)) + 180
        if ang < 0:
            ang += 360
        if 45 <= ang < 135:
            ang = 90
        elif 135 <= ang < 225:
            ang = 180
        elif 225 <= ang < 315:
            ang = 270
        else:
            ang = 0
        return ang

    def load_map(self,ind):
        map_dict=self.map_dicts[ind]
        self.map_sufs=[]
        if 'straight' in map_dict.keys():
            for attr in map_dict['straight']:
                straight = Straight(self.game)
                straight.loc = (attr[0], attr[1])### 0: loc[0], 1: loc[1], 2: ang(, 3: type)
                straight.ang = attr[2]
                self.map_sufs.append(straight)

        if 'impasse' in map_dict.keys():
            for attr in map_dict['impasse']:
                impasse = Impasse(self.game)
                impasse.loc = (attr[0], attr[1])
                impasse.ang = attr[2]
                self.map_sufs.append(impasse)

        if 'turn' in map_dict.keys():
            for attr in map_dict['turn']:
                turn = Turn(self.game)
                turn.loc = (attr[0], attr[1])
                turn.ang = attr[2]
                self.map_sufs.append(turn)

        if 'three' in map_dict.keys():
            for attr in map_dict['three']:
                three = Three(self.game)
                three.loc = (attr[0], attr[1])
                three.ang = attr[2]
                self.map_sufs.append(three)

        if 'four' in map_dict.keys():
            for attr in map_dict['four']:
                four = Four(self.game)
                four.loc = (attr[0], attr[1])
                four.ang = attr[2]
                self.map_sufs.append(four)

        if 'floor' in map_dict.keys():
            for attr in map_dict['floor']:
                floor=Floor(self.game)
                floor.loc= (attr[0], attr[1])
                floor.ang = attr[2]
                self.map_sufs.append(floor)

        if 'arrow' in map_dict.keys():
            for attr in map_dict['arrow']:
                arrow=Arrow(self.game,attr[3:])
                arrow.loc=(attr[0],attr[1])
                arrow.ang=attr[2]
                self.map_sufs.append(arrow)

        start = Start(self.game)
        start.loc = (map_dict['start'][0], map_dict['start'][1])
        start.ang = 0
        self.map_sufs.append(start)

        end = End(self.game)
        end.loc = (map_dict['end'][0], map_dict['end'][1])
        end.ang = 0
        self.map_sufs.append(end)