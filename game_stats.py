from pathlib import Path
import json
class GameStats:
    """Store statistics for the game alien invasion"""
    def __init__(self, ai_game) -> None:
         
         self.settings = ai_game.settings
         self.reset_stats()
         #high score
         self.high_score = self.get_stored_high_score()

    def reset_stats(self):
         self.ships_left = self.settings.ship_limit
         self.score = 0
         self.level = 1

    def get_stored_high_score(self):
         path = Path('stats/high_score.txt')
         content = path.read_text()
         score = json.loads(content)
         return score
         
