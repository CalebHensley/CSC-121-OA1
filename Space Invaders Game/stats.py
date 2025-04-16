class GameStats:
    """Track statistics for Space Invaders."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Space Invaders in an inactive state.
        self.game_active = False
        

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0
        
    def increment_level(self):
        """Increase the level by 1."""
        self.level += 1