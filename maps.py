import json, math
from straight import Straight
from start import Start
from end import End
from impasse import Impasse
from turn import Turn
from three import Three
from four import Four
import pygame

#map loader and manager

class Map_Manager:
    def __init__(self,navigator):
        self.game=navigator.game
        self.RW=self.game.REF_WIDTH
        self.RH=self.game.REF_HEIGHT

        self.back_rect = None
        self.back_suf = pygame.Surface((100, 35))
        self.back_suf.fill((252, 232, 55))
        font=pygame.font.Font('res/font/DroidSansChinese.ttf',30)
        self.back_font = font.render('«返回', True, (0, 0, 0), None)

        map_files=['map1.json','map2.json','map3.json']
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
        if self.back_rect and self.navigator.press_pos and self.back_rect.collidepoint(self.navigator.press_pos):
            self.game.st=4
            self.navigator.press_pos=False
            self.game.beginning=True
            self.navigator.end=None
            self.navigator.moving=False
            return
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
        self.back_rect=self.game.blit_to_sc(self.back_suf,(60,20),0)
        self.game.blit_to_sc(self.back_font,(60,20),0)

    def get_level_num(self):
        return 3

    def judge_action(self):
        ang=self.round_ang()
        action = None
        for suf in self.map_sufs:
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
                break
        if abs(self.navigator.ang-ang)==180:
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
        dx, dy = x - 600 * self.game.w / self.RW, 255 * self.game.h / self.RH - y
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
        if 'straight' in map_dict:
            for attr in map_dict['straight']:
                straight = Straight(self.game)
                straight.loc = (attr[0], attr[1])
                straight.ang = attr[2]
                self.map_sufs.append(straight)

        if 'impasse' in map_dict:
            for attr in map_dict['impasse']:
                impasse = Impasse(self.game)
                impasse.loc = (attr[0], attr[1])
                impasse.ang = attr[2]
                self.map_sufs.append(impasse)

        if 'turn' in map_dict:
            for attr in map_dict['turn']:
                turn = Turn(self.game)
                turn.loc = (attr[0], attr[1])
                turn.ang = attr[2]
                self.map_sufs.append(turn)

        if 'three' in map_dict:
            for attr in map_dict['three']:
                three = Three(self.game)
                three.loc = (attr[0], attr[1])
                three.ang = attr[2]
                self.map_sufs.append(three)

        if 'four' in map_dict:
            for attr in map_dict['four']:
                four = Four(self.game)
                four.loc = (attr[0], attr[1])
                four.ang = attr[2]
                self.map_sufs.append(four)

        start = Start(self.game)
        start.loc = (map_dict['start'][0], map_dict['start'][1])
        start.ang = 0
        self.map_sufs.append(start)

        end = End(self.game)
        end.loc = (map_dict['end'][0], map_dict['end'][1])
        end.ang = 0
        self.map_sufs.append(end)