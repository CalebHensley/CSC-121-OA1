class Settings:
    """A class to store all settings for Space Invaders."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (230, 230, 230)
        self.ship_speed = 2.0
        self.bullet_speed = 5.0  # Adjust as needed
        self.bullet_color = (60, 60, 60)  # Adjust as needed
        self.bullets_allowed = 3  # Adjust as needed
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        self.ship_limit = 3
        self.speedup_scale = 1.05
        self.score_scale = 1.5
        self.alien_points = 50
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that can change during the game."""
        self.ship_speed = 1.1
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.speedup_scale)