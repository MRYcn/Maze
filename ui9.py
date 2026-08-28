import pygame
import pygame.transform as pt


# checkout page

class UI9:
    def __init__(self, game):
        self.game = game

        font1 = pygame.font.Font(self.game.resource_path('res/font/DFPGB_Y5.ttf'), 95)
        font2 = pygame.font.Font(self.game.resource_path('res/font/DFPGB_Y5.ttf'), 45)
        self.result = font1.render(' 过关！', True, (0, 0, 0), None)

        self.back_rect = None
        self.back_suf = pt.scale(pygame.image.load(self.game.resource_path('res/pic/ui0_suf.png')), (200, 70))
        self.back_suf.set_alpha(150)
        self.back_font = font2.render('返回', True, (0, 0, 0), None)

        self.sound_effect = pygame.mixer.Sound(game.resource_path("res/audio/completion.ogg"))
        self.sound_effect.set_volume(0.2)
        self.sound_effect_playing = False

        self.click_effect = game.click_effect

    def display(self):
        self.sound_keeping()
        self.game.blit_to_sc(self.result, (642, 200), 0)
        self.back_rect = self.game.blit_to_sc(self.back_suf, (642, 450), 0)
        self.game.blit_to_sc(self.back_font, (642, 450), 0)

    def update(self, press_pos):
        self.click_effect.play()
        if self.back_rect.collidepoint(press_pos):
            self.game.st = 4
            if self.sound_effect_playing:
                self.sound_effect.stop()
                self.sound_effect_playing = False
            self.game.ui7.coin_all_alpha = 150

    def sound_keeping(self):
        if not self.sound_effect_playing:
            self.sound_effect.play()
            self.sound_effect_playing = True