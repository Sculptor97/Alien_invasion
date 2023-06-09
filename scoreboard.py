import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """Class to display game statistics"""
    def __init__(self, ai_game) -> None:
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font settings
        self.text_color = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """Convert score and and position"""
        #convert score to string
        rounded_score = round(self.stats.score, -1)
        score_str = f'Sc: {rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        #position scoreboard
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """prep high score"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = str(f'Hs: {high_score:,}')
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_rect = self.high_score_image.get_rect()
        self.high_rect.centerx = self.screen_rect.centerx
        self.high_rect.top = self.score_rect.top

    def prep_level(self):
        """prep level"""
        level_str = f'Lv: {self.stats.level}'
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        """Display number of ships left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        """checks for high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def show_score(self):
        """display score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

