import pygame


class Straight:
    def __init__(self, game):
        self.img = pygame.image.load('res/pic/straight.png')
        self.game = game
        self.loc = ()
        self.ang = 0

    def display(self):
        self.game.blit_to_sc(self.img, self.loc, self.ang)
