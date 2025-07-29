import pygame

#signal: waiting for update

class UI6:
    def __init__(self,game):
        self.game=game
        self.back_rect=None
        font1=pygame.font.Font('res/font/DFPGB_Y5.ttf',45)
        self.back=font1.render('<<返回',True,(0,0,0),None)
        texts=[
            '当前版本暂未推出此功',
            '能，请尝试更新软件。'
        ]
        self.signal_texts=[font1.render(text,True,(0,0,0),None) for text in texts]
    
    def display(self):
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)
        y = 250
        for text in self.signal_texts:
            self.game.blit_to_sc(text, (642, y), 0)
            y += 50
    
    def update(self,press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=1