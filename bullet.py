import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    """For properties and behaviour of bullets"""
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed
        #get bullet height and width
        self.width, self.height = self.settings.bullet_width, self.settings.bullet_height
        self.rect = pg.Rect((0,0), (self.width, self.height))
        
        #position the bullet
        self.rect.midtop = ai_game.ship.rect.midtop
        #store bullet's y-value as float for fine control
        self.y = float(self.rect.y)

    def update(self):
        """updates bullet location"""
        #move bullet upward
        self.y -= self.speed
        #update bullet's y-value
        self.rect.y = self.y

    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)
