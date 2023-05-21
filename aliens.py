import sys
import pygame as pg
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage all assets and behaviour of Alien Invasion"""

    def __init__(self) -> None:
        # make pygame resources available
        pg.init()

        # initialize settings
        self.settings = Settings()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_changes()
            self._render_objects()

            # make new changes visible
            pg.display.flip()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """polls for user input"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pg.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pg.K_LEFT:
            self.ship.moving_left = True
        if event.key == pg.K_UP:
            self.ship.moving_up = True
        if event.key == pg.K_DOWN:
            self.ship.moving_down = True
        if event.key == pg.K_q:
            sys.exit()

    def _handle_keyup(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pg.K_LEFT:
            self.ship.moving_left = False
        if event.key == pg.K_UP:
            self.ship.moving_up = False
        if event.key == pg.K_DOWN:
            self.ship.moving_down = False

    def _update_changes(self):
        """update game objects"""
        self.screen.fill(self.settings.bg_color)
        # updates go here
        self.ship.update()

    def _render_objects(self):
        """draw game objects"""
        self.ship.blitme()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
