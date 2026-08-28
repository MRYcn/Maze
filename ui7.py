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
                self.guidance_dict[i + 1] = map_dict['guidance'] #self.guidance_dict[i]中i为级别数
        self.current_guidance_suf_locs = {}
        self.bg = pygame.image.load(game.resource_path('res/pic/game_bg.png'))

        self.coin_back = pygame.image.load(game.resource_path('res/pic/coin_back.png'))
        self.coin_back.set_alpha(150)
        self.coin_sufs = []
        for i in range(1,10):
            img = pygame.image.load(game.resource_path(f'res/pic/coins/coin_{i}.png'))
            self.coin_sufs.append(img)
        self.coin_turn_timer = 0
        self.coin_font = pygame.font.Font(game.resource_path('res/font/DFPGB_Y5.ttf'), 30)
        self.coin_num = self.game.data['data']['coins']
        self.update_coin()
        self.coin_all_alpha = 150
        self.alpha_timer = 0

    def display(self):
        if self.coin_num != self.game.data['data']['coins']:
            self.coin_all_alpha = 150
            self.update_coin()
            self.coin_num = self.game.data['data']['coins']
        self.screen.fill((0, 0, 0))
        self.game.blit_bg(self.bg)
        if self.game.st[1] not in self.current_guidance_suf_locs.keys():
            self.load_gid_sufs(self.game.st[1])
        for suf, loc in self.current_guidance_suf_locs[self.game.st[1]]:
            self.game.blit_to_sc(suf, loc, 0)
        self.navigator.update()
        # self.back_rect=self.game.blit_to_sc(self.back_suf,(60,20),0)
        self.back_rect = self.game.blit_to_sc(self.back_text, (60, 20), 0)

        self.coin_turn_timer += self.game.dt
        if self.coin_turn_timer >= 200:
            self.coin_turn_timer -= 200
            if self.game.coin_count < 9:
                self.game.coin_count += 1
            else:
                self.game.coin_count = 1

        self.alpha_timer += self.game.dt
        if self.coin_all_alpha != 0 and self.alpha_timer >= 50:
            self.alpha_timer -= 50
            self.coin_all_alpha -= 3
            self.coin_back.set_alpha(self.coin_all_alpha)
            self.coin_num_suf.set_alpha(self.coin_all_alpha)
            for suf in self.coin_sufs:
                suf.set_alpha(self.coin_all_alpha)

        self.game.blit_to_sc(self.coin_back, (640, 30), 0)
        self.game.blit_to_sc(self.coin_sufs[self.game.coin_count - 1], (600, 30), 0)
        self.game.blit_to_sc(self.coin_num_suf, (660,28), 0)

    def update(self, press_pos=False, mouse_wheel=False):
        if self.back_rect.collidepoint(press_pos):
            self.game.st = 4
            self.navigator.press_pos = False
            self.game.beginning = True
            self.navigator.end = None
            self.navigator.moving = False
            self.coin_all_alpha = 150
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

    def update_coin(self):
        self.coin_num_suf = self.coin_font.render(str(self.game.data['data']['coins']), True, (0, 0, 0), None)