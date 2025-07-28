import pygame
import webbrowser

#about page

class UI3:
    def __init__(self,game):
        self.game=game
        self.back_rect=self.copy_rect=self.update_rect=None
        font=pygame.font.Font('res/font/DroidSansChinese.ttf',45)
        texts=['软件名：迷宫大挑战',
            '版本：1.0.0',
            '程序设计：Byte豚/MRYcn，美术设计：Lotus_Yi',
            '联系方式：yrk202105152030@outlook.com',
            'License: MIT License',
            '获取更新：联系开发者/访问官网'
            ]
        self.about_texts=[font.render(text,True,(0,0,0),None) for text in texts]
        self.back_text=font.render('«返回',True,(0,0,0),None)

        self.update_suf=pygame.Surface((250,70))
        self.update_suf.fill((255,255,255))
        self.update_text=font.render('访问官网',True,(0,0,0),None)
    
    def display(self):
        y=150
        for text in self.about_texts:
            self.game.blit_to_sc(text,(642,y),0)
            y+=50
        self.back_rect=self.game.blit_to_sc(self.back_text,(125,80),0)
        self.update_rect = self.game.blit_to_sc(self.update_suf, (642, 480), 0)
        self.game.blit_to_sc(self.update_text, (642, 480), 0)
    
    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=0
        elif self.update_rect.collidepoint(press_pos):
            webbrowser.open('https://mrycn.github.io/Maze')