import pygame as pg


class Ship:
    """Class to handle ship properties and behaviour"""
    def __init__(self, ai_game) -> None:
        #get surface 
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        #load ship image
        self.image = pg.image.load('images/ship.bmp').convert()
        self.rect = self.image.get_rect()
        #position the ship
        self.rect.midbottom = self.screen_rect.midbottom
        #store rect's x-value as float
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
         