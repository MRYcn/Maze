import pygame

#user info

class UI10:
    def __init__(self,game):
        self.game=game
        self.back_rect=None
        self.suf2_rect=None
        font1=pygame.font.Font('res/font/DroidSansChinese.ttf',35)
        self.suf1=pygame.image.load('res/pic/username.png')
        self.suf1_text=font1.render('用户名：',True,(0,0,0),None)
        self.username=font1.render(self.game.data['user']['name'],True,(0,0,0),None)
        self.suf2=pygame.image.load('res/pic/suspend.png')
        self.suf2_text=font1.render('注销',True,(0,0,0),None)

        font2 = pygame.font.Font('res/font/DroidSansChinese.ttf', 45)
        self.back = font2.render('«返回', True, (0, 0, 0), None)

    def display(self):
        self.game.blit_to_sc(self.suf1,(342,320),0)
        self.game.blit_to_sc(self.suf1_text,(335,160),0)
        self.game.blit_to_sc(self.username,(300,480),0)
        self.suf2_rect=self.game.blit_to_sc(self.suf2,(600,320),0)
        self.game.blit_to_sc(self.suf2_text,(600,480),0)
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)

    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=5
        elif self.suf2_rect.collidepoint(press_pos):
            self.game.st=11