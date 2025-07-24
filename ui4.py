import pygame

#level selection page

class UI4:
    def __init__(self,game):
        self.game=game
        self.mm=game.navigator.mm

        self.map=self.game.data['data']['map'][::]
        self.suf_rects=[]
        self.back_rect=None
        self.slider_rect=None
        font1=pygame.font.Font('res/font/DroidSansChinese.ttf',45)
        self.back=font1.render('«返回',True,(0,0,0),None)

        self.level_num=self.mm.get_level_num()
        self.sufs=[pygame.Surface((200,400)) for _ in range(self.level_num)]
        self.sufs_init_locs=[(342+i*300,320) for i in range(self.level_num)]
        self.sufs_locs=self.sufs_init_locs[::]
        self.update_color()

        texts=['关卡'+str(i+1) for i in range(self.level_num)]
        self.level_texts=[font1.render(text,True,(0,0,0),None) for text in texts]

        self.slider_back=pygame.Surface((1000,25))
        self.slider_back.fill((221,221,219))
        #self.slider_width=2000/(level_num-1)
        self.slider_width = 2000 / (5 - 1)
        self.slider_init_loc=(142+self.slider_width/2,575)
        self.slider_max_loc=(1142-self.slider_width/2,575)
        self.slider_loc=self.slider_init_loc
        self.slider=pygame.Surface((self.slider_width,25))
        self.slider.fill((107,106,106))


    def display(self):
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)
        self.slider_rect=self.game.blit_to_sc(self.slider_back,(642,575),0)
        self.game.blit_to_sc(self.slider,self.slider_loc,0)

        self.suf_rects=[]
        for i,suf in enumerate(self.sufs):
            self.suf_rects.append(self.game.blit_to_sc(suf,self.sufs_locs[i],0))
            self.game.blit_to_sc(self.level_texts[i],(self.sufs_locs[i][0]-35,480),0)
    
    def update(self,press_pos=False,mouse_wheel=False):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=1
        for i,rect in enumerate(self.suf_rects):
            if rect.collidepoint(press_pos) and (i==0 or i in self.game.data['data']['map']):
                self.game.st=(7,i+1)
                self.mm.load_map(i)
                self.i=i
                break
        if self.slider_rect.collidepoint(press_pos):
            if self.game.w / self.game.h >= 2.19:
                press_pos = (press_pos[0] * self.game.REF_HEIGHT / self.game.h,
                             press_pos[1] * self.game.REF_HEIGHT / self.game.h)
            else:
                press_pos = (press_pos[0] * self.game.REF_WIDTH / self.game.w,
                             press_pos[1] * self.game.REF_WIDTH / self.game.w)
            if press_pos[0]<self.slider_init_loc[0]:
                self.slider_loc=self.slider_init_loc
            elif press_pos[0]>self.slider_max_loc[0]:
                self.slider_loc=self.slider_max_loc
            else:
                self.slider_loc=(press_pos[0],575)
            da=(self.slider_loc[0]-self.slider_init_loc[0])/(self.slider_max_loc[0]-self.slider_init_loc[0])*(300*self.level_num-900)
            self.sufs_locs=[(342+i*300-da,320) for i in range(self.level_num)]
        if self.map!=self.game.data['data']['map']:
            self.update_color()
            self.map = self.game.data['data']['map'][::]

    def update_color(self):
        for i,suf in enumerate(self.sufs):
            if i+1 in self.game.data['data']['map']:
                suf.fill((252,232,55))
            elif i==max(self.game.data['data']['map']):
                suf.fill((242,144,53))
            else:
                suf.fill((168,152,37))