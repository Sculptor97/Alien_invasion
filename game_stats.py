class GameStats:
    """Store statistics for the game alien invasion"""
    def __init__(self, ai_game) -> None:
         
         self.settings = ai_game.settings
         self.reset_stats()

    def reset_stats(self):
         self.ships_left = self.settings.ship_limit