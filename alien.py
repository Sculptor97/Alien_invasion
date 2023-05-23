import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    """Handle the properties and behaviour of aliens"""
    def __init__(self, ai_game) -> None:
        super().__init__()
        #get surface
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.speed = self.settings.alien_speed

        #load image and get rect
        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.width, self.height = self.rect.size

        #place alien at top-left corner with spacing equal its
        #width and height
        self.rect.x = self.width 
        self.rect.y = self.height

        #store x-value as float
        self.x = float(self.rect.x)

    def check_edges(self):
        """check if the aliens have reached the edges"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right > screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        #move alien to the right
        self.x += self.speed*self.settings.fleet_direction
        self.rect.x = self.x
    
        
        