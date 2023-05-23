class Settings:
    """Store all settings for the alien game"""
    def __init__(self) -> None:
         #general settings
         self.screen_width = 800
         self.screen_height = 600
         self.bg_color = (230, 230, 230)
         self.fps = 60

         #ship's settings
         self.ship_speed = 5.5
         self.ship_limit = 3

         #Bullet settings
         self.bullet_speed = 2.5
         self.bullet_width = 5
         self.bullet_height = 15
         self.bullet_color = (60, 60, 60)
         self.bullet_limit = 4

         #alien settings
         self.alien_speed = 1.0
         self.fleet_drop_speed = 20
         #fleet direction 1 indicates moving right and -1 moving left
         self.fleet_direction = 1

         #place aliens at random
         self.start = -50
         self.end = 50