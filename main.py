import sys
from datetime import datetime
import pygame
import pygame.transform as pt

from navigator import Navigator
from ui0 import UI0
from ui1 import UI1
from ui2 import UI2
from ui3 import UI3
from ui4 import UI4
from ui5 import UI5
from ui6 import UI6
from ui9 import UI9
from data import Data_Manager

class Game:
    def __init__(self):
        pygame.init()
        screeninfo=pygame.display.Info()
        self.REF_WIDTH=1285
        self.REF_HEIGHT=586
        width=int(screeninfo.current_w*3/4)
        height=int(screeninfo.current_h*3/4)
        self.screen=pygame.display.set_mode((width,height),pygame.RESIZABLE)
        pygame.display.set_caption('迷宫大作战')
        
        self.clock=pygame.time.Clock()
        self.mouse_leftdown=False
        self.mouse_wheel=False
        self.mouse_pos=False
        self.press_pos=False
        self.gaming=False
        self.screen_size=None
        self.w=self.h=None
        
        self.ui0=UI0(self)
        self.ui1=UI1(self)
        self.ui2=UI2(self)
        self.ui3=UI3(self)
        self.ui5=UI5(self)
        self.ui6=UI6(self)
        self.ui9=UI9(self)
        self.navigator=Navigator(self)
        self.ui4=UI4(self)

        self.st=0
        self.beginning=True

        self.dm=Data_Manager()
        self.on_game_start()
    
    def run(self):
        self.gaming=True
        while self.gaming:
            
            self.check_event()
            if self.gaming:
                self.run_game()
                pygame.display.flip()
                self.clock.tick(60)
        
    def check_event(self):
        self.screen_size=self.screen.get_size()
        self.w=self.screen_size[0]
        self.h=self.screen_size[1]
        self.mouse_pos=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.on_game_exit()
                self.gaming=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button in [4,5]:
                    self.mouse_wheel=event.button
                elif self.mouse_wheel:
                    self.mouse_wheel=False
                else:
                    self.press_pos=self.mouse_pos
    
    def run_game(self):  ##testing
        self.screen.fill((99,205,255))
        if self.st==0:#launch page
            self.ui0.display()
            if self.press_pos:
                self.ui0.update(self.press_pos)
        elif self.st==1:#mode selection page
            self.ui1.display()
            if self.press_pos:
                self.ui1.update(self.press_pos)
        elif self.st==2:#introduction page
            self.ui2.display()
            if self.press_pos:
                self.ui2.update(self.press_pos)
        elif self.st==3:#about page
            self.ui3.display()
            if self.press_pos:
                self.ui3.update(self.press_pos)
        elif self.st==4:#level selection page
            self.ui4.display()
            if self.press_pos:
                self.ui4.update(self.press_pos)
        elif self.st==5:#settings
            self.ui5.display()
            if self.press_pos:
                self.ui5.update(self.press_pos)
        elif self.st==6:#signal: waiting for update
            self.ui6.display()
            if self.press_pos:
                self.ui6.update(self.press_pos)
        elif isinstance(self.st,tuple) and self.st[0]==8:#levels
            self.screen.fill((255,255,255))
            self.navigator.update()
            if self.press_pos:
                self.navigator.press_pos=self.press_pos
        elif self.st==9:
            self.ui9.display()
            if self.press_pos:
                self.ui9.update(self.press_pos)

        self.press_pos=False

     
    def blit_to_sc(self,img,loc,ang):
        """zoom and blit"""
        #loc: center location
        #ang: angle to rotate
        if self.w/self.h>=2.19:
            selfw=self.h*2.19
            selfh=self.h
        else:
            selfw=self.w
            selfh=self.w/2.19
        w,h=img.get_size()
        w=int(w*selfw/self.REF_WIDTH)
        h=int(h*selfh/self.REF_HEIGHT)
        img=pt.scale(img,(w,h))
        img=pt.rotate(img,ang)
        rect=img.get_rect()
        cx=loc[0]*selfw/self.REF_WIDTH
        cy=loc[1]*selfh/self.REF_HEIGHT
        rect.center=(int(cx),int(cy))
        return self.screen.blit(img,rect)

    def on_game_start(self):
        self.data=self.dm.load_data()
        self.data['user']['last_login']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data['user']['is_online']=True
        self.dm.save_data(self.data)

    def on_game_exit(self):
        self.data['user']['is_online']=False
        self.dm.save_data(self.data)

if __name__=='__main__':
    app=Game()
    app.run()
    pygame.quit()
    sys.exit()
