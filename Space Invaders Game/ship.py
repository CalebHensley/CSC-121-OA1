import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
        self.max_health = 3
        self.health = self.max_health

    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right:
             self.rect.x += self.settings.ship_speed
        if self.moving_left:
             self.rect.x -= self.settings.ship_speed
    # If moving right and ship's right edge is less than the screen's right edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
    # If moving left and ship's left edge is greater than the screen's left edge
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
            
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)