import pygame
import pygame.transform as pt

# 设置->偏好

class UI12:
    def __init__(self, game):
        self.game = game
        self.suf1_rect = self.back_rect = None
        font1 = pygame.font.Font(game.resource_path('res/font/DFPGB_Y5.ttf'), 45)
        self.suf1 = pygame.image.load(game.resource_path('res/pic/preference.png'))
        self.suf1.set_alpha(150)
        self.suf1_text = font1.render('方向指引', True, (0, 0, 0), None)

        self.pref_data = game.data['data']['preference']
        self.yes_icon = pygame.image.load(game.resource_path('res/pic/finished_icon.png'))
        self.yes_locs = []

        self.update_pref_status()

        font2 = pygame.font.Font(game.resource_path('res/font/DFPGB_Y5.ttf'), 45)
        self.back = font2.render('<<返回', True, (0, 0, 0), None)

        self.click_effect = game.click_effect

    def display(self):
        self.suf1_rect = self.game.blit_to_sc(self.suf1, (342, 320), 0)
        self.game.blit_to_sc(self.suf1_text, (342,480), 0)
        self.back_rect = self.game.blit_to_sc(self.back, (125,80), 0)
        for loc in self.yes_locs:
            self.game.blit_to_sc(self.yes_icon, (loc[0], loc[1]), 0)

    def update(self, press_pos):
        self.click_effect.play()
        if self.back_rect.collidepoint(press_pos):
            self.game.st = 5
        elif self.suf1_rect.collidepoint(press_pos):
            if self.pref_data['directional_guidance']:
                self.pref_data['directional_guidance'] = False
            else:
                self.pref_data['directional_guidance'] = True

        self.update_pref_status()

    def update_pref_status(self):
        self.yes_locs = []
        for i, key in enumerate(self.pref_data):
            if type(self.pref_data[key]) == bool and self.pref_data[key]:
                loc = (342 + i * 300 + 55, 160)
                self.yes_locs.append(loc)
