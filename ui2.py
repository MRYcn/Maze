import pygame


# introduction page

class UI2:
    def __init__(self, game):
        self.game = game
        self.back_rect = None
        font = pygame.font.Font('res/font/DFPGB_Y5.ttf', 45)
        texts = ['玩家操控车标在2D俯视',
                 '角迷宫中移动，通过选',
                 '择前进方向、利用道路',
                 '层叠、并遵守相关规则，',
                 '完成从起点到终点的既',
                 '定路径。']
        self.intro_texts = [font.render(text, True, (0, 0, 0), None) for text in texts]
        self.back_text = font.render('<<返回', True, (0, 0, 0), None)

    def display(self):
        y = 150
        for text in self.intro_texts:
            self.game.blit_to_sc(text, (642, y), 0)
            y += 50
        self.back_rect = self.game.blit_to_sc(self.back_text, (125, 80), 0)

    def update(self, press_pos):
        if self.back_rect.collidepoint(press_pos):
            self.game.st = 0
