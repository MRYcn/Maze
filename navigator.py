import pygame
import math

from maps import Map_Manager

#navigator image and manager

class Navigator:
    def __init__(self,game):
        self.img=pygame.image.load('res/pic/navigator.png')
        self.game=game
        self.RW=game.REF_WIDTH
        self.RH=game.REF_HEIGHT
        self.loc=(600,255)
        self.ang=90
        self.press_pos=False
        self.moving=False
        
        self.mm=Map_Manager(self)
        self.end=None
    
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
                        break
        if self.end.loc==(600,255):
            self.game.st=9
            self.end=None
            self.game.beginning=True
            return
            
        self.mm.display()
        
        self.game.blit_to_sc(self.img,self.loc,-90+self.ang)
            
    def update0(self):
        x,y=self.game.mouse_pos
        dx,dy=x-600*self.game.w/self.RW,255*self.game.h/self.RH-y
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
