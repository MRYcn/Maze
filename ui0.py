import pygame

#launch page

class UI0:
    def __init__(self,game):
        self.game=game
        self.suf1_rect=self.suf2_rect=self.suf3_rect=self.title_rect=None
        font1=pygame.font.Font('res/font/DroidSansChinese.ttf',45)
        self.suf1=pygame.Surface((250,70))
        self.suf1.fill((255,255,255))
        self.suf1.set_alpha((150))
        self.suf1_text=font1.render('开始游戏',True,(0,0,0),None)
        self.suf2=pygame.Surface((200,70))
        self.suf2.fill((255,255,255))
        self.suf2.set_alpha((150))
        self.suf2_text=font1.render('介绍',True,(0,0,0),None)
        self.suf3=pygame.Surface((200,70))
        self.suf3.fill((255,255,255))
        self.suf3.set_alpha((150))
        self.suf3_text=font1.render('关于',True,(0,0,0),None)
        title_font=pygame.font.Font('res/font/华文行楷.ttf',95)
        self.title=title_font.render('迷宫大挑战',True,(255,123,1),None)
        self.scale_text=font1.render('将窗口拉伸至2:1（看不见这行字）以获得最佳体验',True,(0,0,0),None)
    
    def display(self):
        self.suf1_rect=self.game.blit_to_sc(self.suf1,(642,450),0)
        self.game.blit_to_sc(self.suf1_text,(642,450),0)
        self.suf2_rect=self.game.blit_to_sc(self.suf2,(342,450),0)
        self.game.blit_to_sc(self.suf2_text,(342,450),0)
        self.suf3_rect=self.game.blit_to_sc(self.suf3,(942,450),0)
        self.game.blit_to_sc(self.suf3_text,(942,450),0)
        self.title_rect=self.game.blit_to_sc(self.title,(642,200),0)
        self.game.blit_to_sc(self.scale_text,(642,660),0)
    
    def update(self,press_pos):
        if self.suf1_rect.collidepoint(press_pos):
            self.game.st=1
        elif self.suf2_rect.collidepoint(press_pos):
            self.game.st=2
        elif self.suf3_rect.collidepoint(press_pos):
            self.game.st=3