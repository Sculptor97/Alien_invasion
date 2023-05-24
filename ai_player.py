import pygame
from random import random
from alien_invasion import AlienInvasion


class AIPlayer:
    """Automatic player for alien Invasion"""
    def __init__(self, ai_game) -> None:
        #pass the ai_game object
        self.ai_game = ai_game

    def run_game(self):
        """Replaces the original run_game so we can interject our own controls"""
        #start out game in active state and hide the mouse
        self.ai_game.game_active = True
        pygame.mouse.set_visible(False)

        #modify game speed for development purposes
        self._modify_speed(10)
        #get the fleet size
        self.fleet_size = len(self.ai_game.aliens)
        while True:
            self.ai_game._check_events()
            self._implement_strategy()

            if self.ai_game.game_active:
                self.ai_game._update_changes()
            self.ai_game._render_objects()

    def _implement_strategy(self):
        """Move the ship left and right while firing bullets"""
        #get target alien
        target_alien = self._get_target_alien()
        ship = self.ai_game.ship
        if ship.rect.x < target_alien.rect.x:
            ship.moving_right = True
            ship.moving_left = False
        elif ship.rect.x > target_alien.rect.x:
            ship.moving_right = False
            ship.moving_left = True

        #freeze ship if fleet size is half
        # if len(self.ai_game.aliens) >= 0.5*self.fleet_size:
        #     self._sweep_left_right()
        # else:
        #     self.ai_game.ship.moving_right = False
        #     self.ai_game.ship.moving_left = False

        #fire bullet at a random frequency whenever possible
        firing_frequency = 1.0
        if random() < firing_frequency:
            self.ai_game._fire_bullet()
    def _get_target_alien(self):
        """Returns the rightmost alien at the bottom of the fleet"""
        #get the first alien from the fleet
        target_alien = self.ai_game.aliens.sprites()[0]
        for alien in self.ai_game.aliens.sprites():
            if alien.rect.y > target_alien.rect.y:
                target_alien = alien
            elif alien.rect.y < target_alien.rect.y:
                continue
            elif alien.rect.x > target_alien.rect.x:
                target_alien = alien

        return target_alien
    
    def _sweep_left_right(self):
        """move ship left and right"""
        #get the ship instance from ai_game
        ship = self.ai_game.ship
        screen_rect = self.ai_game.screen.get_rect()
        #check if ship is not moving if yes move it to the right
        if not ship.moving_right and not ship.moving_left:
            ship.moving_right = True
        elif (ship.moving_right and ship.rect.right > screen_rect.right - 10):
            ship.moving_right = False
            ship.moving_left = True
        elif ship.moving_left and ship.rect.left < 10:
            ship.moving_left = False
            ship.moving_right = True

    def _modify_speed(self, speed_factor):
        """speed up the game after every level"""
        self.ai_game.settings.ship_speed *= speed_factor
        self.ai_game.settings.bullet_speed *= speed_factor
        self.ai_game.settings.alien_speed *= speed_factor
        

if __name__ == "__main__":
    ai_game = AlienInvasion()

    ai_player = AIPlayer(ai_game)
    ai_player.run_game()
        