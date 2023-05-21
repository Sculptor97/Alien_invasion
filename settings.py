class Settings:
    """Store all settings for the alien game"""
    def __init__(self) -> None:
         #general settings
         self.screen_width = 800
         self.screen_height = 600
         self.bg_color = (230, 230, 230)
         self.fps = 60

         #ship's settings
         self.ship_speed = 2.5

         #Bullet settings
         self.bullet_speed = 2.5
         self.bullet_width = 3
         self.bullet_height = 15
         self.bullet_color = (60, 60, 60)
         self.bullet_limit = 4