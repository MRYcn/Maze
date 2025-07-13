import pygame

#level selection page

class UI4:
    def __init__(self,game):
        self.game=game
        self.mm=game.navigator.mm

        self.suf_rects=[]
        self.back_rect=None
        font1=pygame.font.Font('res/font/DroidSansChinese.ttf',45)
        self.back=font1.render('«返回',True,(0,0,0),None)

        level_num=self.mm.get_level_num()
        self.sufs=[pygame.Surface((200,400)) for _ in range(level_num)]
        for suf in self.sufs:
            suf.fill((252,232,55))

        texts=['关卡'+str(i+1) for i in range(level_num)]
        self.level_texts=[font1.render(text,True,(0,0,0),None) for text in texts]

    def display(self):
        self.back_rect=self.game.blit_to_sc(self.back,(125,80),0)

        self.suf_rects=[]
        x=342
        y=320
        for suf,text in zip(self.sufs,self.level_texts):
            self.suf_rects.append(self.game.blit_to_sc(suf,(x,y),0))
            self.game.blit_to_sc(text,(x-35,480),0)
            x+=300
    
    def update(self,press_pos=False,mouse_wheel=False):
        if self.back_rect.collidepoint(press_pos):
            self.game.st=1
        for i,rect in enumerate(self.suf_rects):
            if rect.collidepoint(press_pos):
                self.game.st=(8,i+1)
                self.mm.load_map(i)
                break