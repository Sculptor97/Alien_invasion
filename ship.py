import pygame as pg


class Ship:
    """Class to handle ship properties and behaviour"""
    def __init__(self, ai_game) -> None:
        #get surface 
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        #load ship image
        self.image = pg.image.load('images/ship.bmp').convert()
        self.rect = self.image.get_rect()
        self.speed = self.settings.ship_speed
        #position the ship
        self.rect.midbottom = self.screen_rect.midbottom
        #store rect's x-value as float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #moving flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        if self.moving_up and self.rect.y > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        #update rect values
        self.rect.x = self.x
        self.rect.y = self.y
        
    def center_ship(self):
        """Center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
         