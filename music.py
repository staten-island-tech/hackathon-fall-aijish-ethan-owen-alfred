import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up game variables
screen_width = 600
screen_height = 800
tile_width = 200
tile_height = 100
fall_speed = 5

# Colors
TILE_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (255, 105, 180)  # Hot Pink

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Piano Tiles')

# Define the font for score and game over text
font = pygame.font.Font(None, 48)

# Tile class
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, tile_width, tile_height)

    def move(self):
        self.y += fall_speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(screen, TILE_COLOR, self.rect, border_radius=10)

# Game loop
def run_game():
    tiles = []
    score = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BACKGROUND_COLOR)  # Background fill

        # Draw lane dividers
        for x in range(1, 3):
            pygame.draw.line(screen, (0, 0, 0), (x * tile_width, 0), (x * tile_width, screen_height), 5)

        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for tile in tiles:
                    if event.key == pygame.K_a and tile.x == 0 and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_s and tile.x == tile_width and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_d and tile.x == 2 * tile_width and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break

        # Add new tiles randomly
        if len(tiles) == 0 or tiles[-1].y > tile_height:
            x_pos = random.randint(0, 2) * tile_width
            new_tile = Tile(x_pos, -tile_height)
            tiles.append(new_tile)

        # Move and draw tiles
        for tile in tiles:
            tile.move()
            tile.draw()

        # Remove tiles that have fallen off the screen
        tiles = [tile for tile in tiles if tile.y < screen_height]

        # Draw the score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Check for game over
        for tile in tiles:
            if tile.y + tile_height >= screen_height:
                running = False

        pygame.display.flip()

        # Frame rate
        clock.tick(60)

    # Game over screen
    game_over_text = font.render("Game Over!", True, (0, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.fill(BACKGROUND_COLOR)
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 50))
    screen.blit(final_score_text, (screen_width // 2 - 150, screen_height // 2 + 50))
    pygame.display.flip()

    # Pause for 3 seconds before quitting
    time.sleep(3)

    pygame.quit()

    restart_button = Button("Restart", screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)

    screen.fill(BACKGROUND_COLOR)
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 50))
    screen.blit(final_score_text, (screen_width // 2 - 150, screen_height // 2 + 10))
    restart_button.draw()
    pygame.display.flip()

    # Wait for user interaction to restart
    restart_clicked = False
    while not restart_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Check if the restart button is clicked
        if restart_button.is_clicked():
            restart_clicked = True

        pygame.display.update()

    # Restart the game
    run_game()

if __name__ == "__main__":
    run_game()
  