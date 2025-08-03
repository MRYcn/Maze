import pygame


class Arrow:
    def __init__(self, game, type):
        self.game = game
        self.type = type[0]
        try:
            self.flip = type[1]
        except:
            self.flip = False
        self.img = pygame.image.load(game.resource_path(f'res/pic/{self.type}.png'))
        self.loc = ()
        self.ang = 0

    def display(self):
        self.game.blit_to_sc(self.img, self.loc, self.ang, self.flip)
