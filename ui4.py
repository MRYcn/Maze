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
        font1=pygame.font.Font('res/font/DFPGB_Y5.ttf',45)
        self.back=font1.render('<<返回',True,(0,0,0),None)

        self.level_num=self.mm.get_level_num()
        self.sufs=[pygame.Surface((200,400)) for _ in range(self.level_num)]
        for i in range(self.level_num):
            self.sufs[i]=pygame.image.load(f'res/pic/level{i+1}.png')
            #self.sufs[i].set_alpha((150))
        self.sufs_init_locs=[(342+i*300,320) for i in range(self.level_num)]
        self.sufs_locs=self.sufs_init_locs[::]

        texts=['关卡'+str(i+1) for i in range(self.level_num)]
        self.level_texts=[font1.render(text,True,(0,0,0),None) for text in texts]

        self.update_progress()
        self.finished_icon=pygame.image.load('res/pic/finished_icon.png')

        self.slider_back=pygame.Surface((1000,25))
        self.slider_back.fill((221,221,219))
        self.slider_back.set_alpha(150)
        self.slider_width = 2000 / (5 - 1)
        self.slider_init_loc=(142+self.slider_width/2,575)
        self.slider_max_loc=(1142-self.slider_width/2,575)
        self.slider_loc=self.slider_init_loc
        self.slider=pygame.Surface((self.slider_width,25))
        self.slider.fill((107,106,106))
        font2=pygame.font.Font('res/font/DFPGB_Y5.ttf',25)
        self.slider_text=font2.render('点击（非长按）以移动滚动条',True,(0,0,0),None)


    def display(self):
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)
        self.slider_rect=self.game.blit_to_sc(self.slider_back,(642,575),0)
        self.game.blit_to_sc(self.slider,self.slider_loc,0)
        self.game.blit_to_sc(self.slider_text,(642,615),0)

        self.suf_rects=[]
        for i,suf in enumerate(self.sufs):
            self.suf_rects.append(self.game.blit_to_sc(suf,self.sufs_locs[i],0))
            self.game.blit_to_sc(self.level_texts[i],(self.sufs_locs[i][0]-30,480),0)
        for loc in self.finished_locs:
            self.game.blit_to_sc(self.finished_icon,loc,0)
    
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
            self.finished_locs=[(self.sufs_locs[i][0]+55,160) for i in range((len(self.finished_locs)))]
        if self.map!=self.game.data['data']['map']:
            self.map = self.game.data['data']['map'][::]

    def update_progress(self):
        self.finished_locs=[]
        for i,loc in enumerate(self.sufs_locs):
            loc=(loc[0]+55,160)
            if i+1 in self.game.data['data']['map']:
                self.finished_locs.append(loc)