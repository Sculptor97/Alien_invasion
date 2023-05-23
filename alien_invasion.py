import sys
import pygame as pg
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from pathlib import Path
import json
import sound_effects as se






class AlienInvasion:
    """Class to manage all assets and behaviour of Alien Invasion"""

    def __init__(self) -> None:
        # make pygame resources available
        pg.init()

        # initialize settings
        self.settings = Settings()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width, self.settings.screen_height = self.screen.get_rect().size
        pg.display.set_caption('Alien Invasion')
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()
        self._create_fleet()
        self.game_active = False
        self.play_button = Button(self,'Play')
        self.sb = Scoreboard(self)

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self._update_changes()
            self._render_objects()

            # make new changes visible
            pg.display.flip()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """polls for user input"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._store_high_score()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pg.KEYUP:
                self._handle_keyup(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _store_high_score(self):
        """save high score to file"""
        path = Path('stats/high_score.txt')
        content = json.dumps(self.stats.high_score)
        path.write_text(content)

    def _check_play_button(self, mouse_pos):
        """Checks if mouse is focused on the playbutton"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #reset the game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()
            self.game_active = True

            #clear the screen
            self.bullets.empty()
            self.aliens.empty()
            #create new fleet
            self._create_fleet()
            self.ship.center_ship()
            #hide the mouse cursor
            pg.mouse.set_visible(False)

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
            self._store_high_score()
            sys.exit()
        if event.key == pg.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        # check number of bullets in group before creating
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            se.bullet_sound.play()

    def _create_fleet(self):
        """create a fleet of aliens"""
        # create alien instance
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height -8*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            #finished a row, reset x-value and increment y
            current_x = alien_width
            current_y += 2*alien_height

    def _create_alien(self, x_position, y_position):
        # create new alien
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position  
        new_alien.rect.y= y_position 
        self.aliens.add(new_alien)

    def _ran(self):
         """returns a random number to offset alien positions"""
         ran = randint(self.settings.start, self.settings.end)
         return ran
    
    def _check_fleet_edges(self):
        """check if alien is on either side of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """drop the entire fleet and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


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
        self._update_bullets()
        self._update_aliens()

    def _update_bullets(self):
        """updates bullet position and removes old ones"""
        #update position
        self.bullets.update()
        #remove old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        #check for collisions between bullet and aliens
        self._check_alien_bullet_collisions()
         
    def _check_alien_bullet_collisions(self):

        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)
        #no more aliens?
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #increase level
            self.stats.level += 1
            self.sb.prep_level()
        #increment score if alien's been hit
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points*len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            se.alien_sound.play()

    def _check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                se.alien_ship.play()
                self._ship_hit()
                break 

    def _ship_hit(self):
        """Respond to ship hits"""
        if self.stats.ships_left > 0:
            #decrement number of ships
            self.stats.ships_left -= 1
            self.sb.prep_ship()

            #destroy any remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()
            #create a new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.game_active = False
            pg.mouse.set_visible(True)

    def _update_aliens(self):
        """check if alien is at either edge then update position of aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        #check for alien-ship collisions
        if pg.sprite.spritecollideany(self.ship, self.aliens):
             se.alien_ship.play()
             self._ship_hit()
        self._check_alien_bottom()

    def _render_objects(self):
        """draw game objects"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #show scoreboard
        self.sb.show_score()
        #draw button to screen if game not active
        if not self.game_active:
            self.play_button.draw_button()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
