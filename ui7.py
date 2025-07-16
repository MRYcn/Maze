import pygame
import pygame.transform as pt

#game page

class UI7:
    def __init__(self,game):
        self.game=game
        self.navigator=game.navigator
        self.screen=game.screen
        self.back_rect=None
        self.font = pygame.font.Font('res/font/DroidSansChinese.ttf', 30)
        self.back_text = self.font.render('«返回', True, (0, 0, 0), None)
        self.back_suf = pygame.Surface((100, 35))
        self.back_suf.fill((252, 232, 55))
        self.guidance_dict={
            1:[
                ['navigator',(60,100)],
                ['：车标',(135,100)],
                ['straight',(60,150)],
                ['：黑线为道路',(185,150)],
                ['边，中间为道路',(185,200)],
                ['start',(60,250)],
                ['：起点',(135,250)],
                ['end',(60,300)],
                ['：终点',(135,300)],
                ['尝试在车标右',(1050,100)],
                ['侧点击屏幕，',(1050,150)],
                ['使车标前进。',(1050,200)]
            ],
            2:[
                ['车标可以在道路中',(1050,100)],
                ['前进。游戏开始时',(1050,150)],
                ['你可以选择行驶方',(1050,200)],
                ['向，开始后将不能',(1050,250)],
                ['调头（180°旋转）',(1050,300)]
            ]
        }
        self.current_guidance_suf_locs={}

    def display(self):
        self.screen.fill((255,255,255))
        if self.game.st[1] not in self.current_guidance_suf_locs.keys():
            self.load_gid_sufs(self.game.st[1])
        for suf,loc in self.current_guidance_suf_locs[self.game.st[1]]:
            self.game.blit_to_sc(suf,loc,0)
        self.navigator.update()
        self.back_rect=self.game.blit_to_sc(self.back_suf,(60,20),0)
        self.game.blit_to_sc(self.back_text,(60,20),0)

    def update(self,press_pos=False,mouse_wheel=False):
        if self.back_rect.collidepoint(press_pos):
            self.game.st = 4
            self.navigator.press_pos = False
            self.game.beginning = True
            self.navigator.end = None
            self.navigator.moving = False
        else:
            self.navigator.press_pos=press_pos

    def load_gid_sufs(self,level):
        self.current_guidance_suf_locs[level]=[]
        if level not in self.guidance_dict.keys():
            return
        for i in self.guidance_dict[level]:
            if i[0]=='start':
                suf=pt.scale(pygame.image.load('res/pic/start.png'),(35,35))
            elif i[0]=='end':
                suf=pt.scale(pygame.image.load('res/pic/end.png'),(35,35))
            elif i[0]=='straight':
                suf=pt.scale(pygame.image.load('res/pic/straight.png'),(35,35))
            elif i[0]=='navigator':
                suf=pt.scale(pygame.image.load('res/pic/navigator.png'),(55,55))
            else:
                suf=self.font.render(i[0],True,(0,0,0),None)
            loc=i[1]
            self.current_guidance_suf_locs[level].append((suf,loc))
