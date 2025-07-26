import pygame
import math

from maps import Map_Manager

#navigator image and manager

class Navigator:
    def __init__(self,game):
        self.img=pygame.image.load('res/pic/navigator.png')
        self.img.set_alpha(200)
        self.game=game
        self.RW=game.REF_WIDTH
        self.RH=game.REF_HEIGHT
        self.loc=(600,255)
        self.ang=90
        self.press_pos=False
        self.moving=False
        
        self.mm=Map_Manager(self)
        self.end=None
        self.start=None
    
    def update(self):#st:game.st
        self.mm.update()
        if self.game.st==4:
            return
        if self.game.beginning:
            self.update0()
            if not self.end:
                for suf in self.mm.map_sufs:
                    if suf.__class__.__name__=='End':
                        self.end=suf
        if self.end and self.end.loc==(600,255):
            self.game.st=9
            self.end=None
            self.game.beginning=True
            if self.game.ui4.i+1 not in self.game.data['data']['map']:
                self.game.data['data']['map'].append(self.game.ui4.i+1)
                self.game.ui4.update_color()
            return
            
        self.mm.display()
        if self.end:
            self.game.draw_line((255,0,0),self.loc,self.end.loc,2)
        self.game.blit_to_sc(self.img,self.loc,-90+self.ang)
            
    def update0(self):
        x,y=self.game.mouse_pos
        if self.game.w / self.game.h >= 2.19:
            x,y=x * self.RH / self.game.h, y * self.RH / self.game.h
        else:
            x,y=x * self.game.REF_WIDTH / self.game.w,y * self.game.REF_WIDTH / self.game.w
        dx,dy=x-600,255-y
        if dx==0:
            if dy>0:
                ang=90
            else:
                ang=-90
        elif dx>0:
            ang=math.degrees(math.atan(dy/dx))
        else:
            ang=math.degrees(math.atan(dy/dx))+180
        if ang<0:
            ang+=360
        self.ang=ang
