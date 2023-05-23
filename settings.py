class Settings:
    """Store all settings for the alien game"""
    def __init__(self) -> None:
         #general settings
         self.screen_width = 1000
         self.screen_height = 800
         self.bg_color = (230, 230, 230)
         self.fps = 60

         #ship's settings
         self.ship_limit = 3

         #Bullet settings
         self.bullet_width = 3
         self.bullet_height = 15
         self.bullet_color = (60, 60, 60)
         self.bullet_limit = 3

         #alien settings
         self.fleet_drop_speed = 10
         
         #place aliens at random
         self.start = -50
         self.end = 50

         self.speed_up_scale = 1.3
         self.score_scale = 1.5
         self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.bullet_speed = 2.5
        self.alien_speed = 2.0
        self.ship_speed = 5.0
        self.alien_points = 50

        #fleet direction 1 indicates moving right and -1 moving left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.ship_speed *= self.speed_up_scale
        self.alien_points = int(self.alien_points*self.score_scale)
         