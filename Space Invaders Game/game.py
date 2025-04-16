import pygame
import sys
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from stats import GameStats
from button import Button
from scoreboard import Scoreboard
import random
import time

DROP_ALIEN_EVENT = pygame.USEREVENT + 1


class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        original_image = pygame.image.load('images/Background.jpg')
        self.bg_image = pygame.transform.scale(original_image, (self.settings.screen_width, self.settings.screen_height))
        pygame.time.set_timer(DROP_ALIEN_EVENT, 5000)
        

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_image = pygame.image.load('images/Background.jpg')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = Group()
        self.aliens = Group()
        self._create_fleet()
        self.score = self.stats.score
        self.health = self.ship.health
        self.font = pygame.font.Font(None, 72)  # Choose the font for the text
        self.stage = self.stats.level
        self.stage_start_time = pygame.time.get_ticks()
        self.scoreboard = Scoreboard(self)
        
        self.play_button = Button(self, "Play")
        
    def _start_game(self):
        """Start a new game."""
        # Reset game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Reset the game settings.
        self.settings.initialize_dynamic_settings()
        self.settings.increase_speed()

        # Reset the ship's health.
        self.ship.health = self.ship.max_health

        # Empty the list of bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
        
        self.scoreboard.prep_level()
        self.scoreboard.prep_score()

        # Reset the play button's label.
        self.play_button.msg = "Play"
        self.play_button._prep_msg(self.play_button.msg)

        
    def _reset_game(self):
        """Reset the game state to start a new game."""
        # Reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True

        # Reset the game objects
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            
            if not self.aliens:
                    self.bullets.empty()
                    self._create_fleet()
                    self.settings.increase_speed()
                    self.font = pygame.font.Font(None, 72)
                    self.stage += 1  # Increment the stage
                    self.stage_start_time = pygame.time.get_ticks()

            
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
            if collisions:
                self.score += len(collisions)  # Grant 1 point for each alien destroyed
                
                # Repopulate the fleet if all aliens have been destroyed
            if not self.aliens:
                self.bullets.empty()
                self._create_fleet()
                self.settings.bullet_speed *= 1.1  # Speed up bullets
                
                 # Check if any aliens have reached the bottom of the screen
            for alien in self.aliens.sprites():
                if alien.rect.bottom >= self.screen.get_rect().bottom:
                    self.health -= 1  # Damage the player
                    break
                
            self.scoreboard.prep_level()
            self.scoreboard.show_score()
            
    def _create_fleet(self):
        """create the fleet of aliens"""
        #create an alien and keep adding aliens until there no room left.
        #space between aliens is one aliens width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        for _ in range(4):  # Limit the number of rows to 4
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            #finished a row; reset x value increment y value
            current_x = alien_width
            current_y += 2 * alien_height
        self.aliens.add(alien)
        
        self.settings.alien_speed *= 1.1
        
        random_alien = random.choice([alien for alien in self.aliens])
        random_alien.move_downwards_only = True
        
        self.stats.increment_level()


    def _create_alien(self, x_position, y_position):
        """create an alien and place it on the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
             self._change_fleet_direction()
             break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.rect.collidepoint(mouse_pos):
                    self._start_game()
                    self.play_button.msg = "Play"
                    self.play_button._prep_msg(self.play_button.msg)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
            elif event.type == DROP_ALIEN_EVENT:
                # Select a random alien and make it start moving downwards.
                random_alien = random.choice(self.aliens.sprites())
                random_alien.start_moving_downwards()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self._fire_bullet()
                    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Reset the scoreboard images.
            self.sb.prep_score()
            self.sb.prep_level()
                    
    def _drop_random_alien(self):
        """Select a random alien and make it start moving downwards."""
        if self.aliens:  # Check if there are any aliens left
            random_alien = random.choice(self.aliens.sprites())
            random_alien.start_moving_downwards()
            
    def _draw_health_bar(self):
        """Draw the health bar indicating the player's life points."""
        if self.stats.ships_left > 0:
            pygame.draw.rect(self.screen, (0, 255, 0), (10, self.settings.screen_height - 20, 100 * (self.stats.ships_left / 3), 10))
            pygame.draw.rect(self.screen, (255, 0, 0), (10 + 100 * (self.stats.ships_left / 3), self.settings.screen_height - 20, 100 * (1 - self.stats.ships_left / 3), 10))
                    

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the positions of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions()
                
    def _ship_hit(self):
        # Look for alien-ship collisions.
        alien_hit = pygame.sprite.spritecollideany(self.ship, self.aliens)
        if alien_hit:
            # Remove the alien that hit the ship.
            self.aliens.remove(alien_hit)
        
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            
            self.bullets.empty()

            # Pause.
            time.sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += 10 * len(aliens)  # Increase score by 10 for each alien destroyed
            self.scoreboard.prep_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
                
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
    
        if self.health <= 1:
            self._game_over()
        
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self.aliens.remove(alien)
                self._ship_hit()
                break

    # Repopulate the fleet if all aliens have been destroyed
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase stage
            self.stage += 1
            self.stage_start_time = pygame.time.get_ticks()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.blit(self.bg_image, (0, 0))
        
        self.ship.blitme()
        self.bullets.draw(self.screen)
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.scoreboard.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
    def _game_over(self):
        """End the current game and show the game over screen."""
        self.stats.game_active = False
        self.health = 1
        pygame.mouse.set_visible(True)
        self.play_button.msg = "Restart"
        self.play_button._prep_msg(self.play_button.msg)

        # Draw the game over screen
        self.screen.fill((0, 0, 0))
        background = pygame.image.load('images/earth.jpg')
        self.screen.blit(background, (0, 0))
        game_over_text = self.font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.settings.screen_width / 2 - game_over_text.get_width() / 2, self.settings.screen_height / 2 - game_over_text.get_height() / 2))
        
        restart_text = self.font.render("Press Enter to restart", True, (255, 255, 255))
        self.screen.blit(restart_text, (self.settings.screen_width / 2 - restart_text.get_width() / 2, self.settings.screen_height / 2 - restart_text.get_height() / 2 + 100))  # Increase the value added to adjust the vertical position

        pygame.display.flip()

        # Wait for the player to press the Enter key
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # The Enter key was pressed
                        self._reset_game()  # Reset the game state
                        return True

if __name__ == "__main__":
    SpaceInvaders().run_game()