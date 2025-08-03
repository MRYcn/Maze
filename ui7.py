import pygame
import pygame.transform as pt


# game page

class UI7:
    def __init__(self, game):
        self.game = game
        self.navigator = game.navigator
        self.screen = game.screen
        self.back_rect = None
        self.font = pygame.font.Font(game.resource_path('res/font/DFPGB_Y5.ttf'), 30)
        self.back_text = self.font.render('<<返回', True, (0, 0, 0), None)
        # self.back_suf = pt.scale(pygame.image.load('res/pic/ui0_suf.png'),(110,35))
        # self.back_suf.set_alpha(100)
        self.guidance_dict = {}
        for i, map_dict in enumerate(self.navigator.mm.map_dicts):
            if 'guidance' in map_dict.keys():
                self.guidance_dict[i + 1] = map_dict['guidance']
        self.current_guidance_suf_locs = {}
        self.bg = pygame.image.load(game.resource_path('res/pic/game_bg.png'))

    def display(self):
        self.screen.fill((0, 0, 0))
        self.game.blit_bg(self.bg)
        if self.game.st[1] not in self.current_guidance_suf_locs.keys():
            self.load_gid_sufs(self.game.st[1])
        for suf, loc in self.current_guidance_suf_locs[self.game.st[1]]:
            self.game.blit_to_sc(suf, loc, 0)
        self.navigator.update()
        # self.back_rect=self.game.blit_to_sc(self.back_suf,(60,20),0)
        self.back_rect = self.game.blit_to_sc(self.back_text, (60, 20), 0)

    def update(self, press_pos=False, mouse_wheel=False):
        if self.back_rect.collidepoint(press_pos):
            self.game.st = 4
            self.navigator.press_pos = False
            self.game.beginning = True
            self.navigator.end = None
            self.navigator.moving = False
        else:
            self.navigator.press_pos = press_pos

    def load_gid_sufs(self, level):
        self.current_guidance_suf_locs[level] = []
        if level not in self.guidance_dict.keys():
            return
        for i in self.guidance_dict[level]:
            if i[0] == 'start':
                suf = pt.scale(pygame.image.load(self.game.resource_path('res/pic/start.png')), (35, 35))
            elif i[0] == 'end':
                suf = pt.scale(pygame.image.load(self.game.resource_path('res/pic/end.png')), (35, 35))
            elif i[0] == 'straight':
                suf = pt.scale(pygame.image.load(self.game.resource_path('res/pic/straight.png')), (35, 35))
            elif i[0] == 'navigator':
                suf = pt.scale(pygame.image.load(self.game.resource_path('res/pic/navigator.png')), (55, 55))
            else:
                suf = self.font.render(i[0], True, (0, 0, 0), None)
            loc = i[1]
            self.current_guidance_suf_locs[level].append((suf, loc))
