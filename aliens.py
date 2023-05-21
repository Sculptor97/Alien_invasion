import sys
import pygame as pg
from settings import Settings

class AlienInvasion:
    """Class to manage all assets and behaviour of Alien Invasion"""
    def __init__(self) -> None:
        #make pygame resources available
        pg.init()

        #initialize settings
        self.settings = Settings()

        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption('Alien Invasion')
        

        

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            #game logic goes here


            self.screen.fill(self.settings.bg_color)

            #Render game objects here


            pg.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

