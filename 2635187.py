import pygame
import random
import time

<<<<<<< HEAD
from time import sleep

# Initialize the pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load("toi.mp3")

# Play the MP3 file
pygame.mixer.music.play()

# Initialize Pygame
pygame.init()


# Set up game variables
=======

pygame.init()
>>>>>>> aijish
screen_width = 600
screen_height = 800
tile_width = 200
tile_height = 100
<<<<<<< HEAD
fall_speed = 7


# Colors
TILE_COLOR = (0, 0, 255)
BACKGROUND_COLOR = (250,105,180)  


# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Piano Tiles')


# Define the font for score and game over text
font = pygame.font.Font(None, 48)


# Tile class
=======
fall_speed = 3
speed_increase_interval = 5000


# Initialize the pygame mixer
pygame.mixer.init()


# Load the MP3 file
pygame.mixer.music.load("toi.mp3")


# Play the MP3 file
pygame.mixer.music.play()


tiles = (0, 0, 0) #black
background = (255, 105, 180) #hot pink


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Music Squares')


font = pygame.font.Font(None, 48)


>>>>>>> aijish
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, tile_width, tile_height)


    def move(self):
        self.y += fall_speed
        self.rect.y = self.y


<<<<<<< HEAD
    def draw(self):
        pygame.draw.rect(screen, TILE_COLOR, self.rect, border_radius=10)


# Game loop
def run_game():
=======
    def draw(self, is_pressed=False):
        color = (0, 200, 0) if is_pressed else tiles
        pygame.draw.rect(screen, color, self.rect, border_radius=10)


def run_game():
    global fall_speed  # Ensure fall_speed can be modified globally
   
>>>>>>> aijish
    tiles = []
    score = 0
    running = True
    clock = pygame.time.Clock()


<<<<<<< HEAD
    while running:
        screen.fill(BACKGROUND_COLOR)  # Background fill


        # Draw lane dividers
        for x in range(1, 3):
            pygame.draw.line(screen, (0, 0, 0), (x * tile_width, 0), (x * tile_width, screen_height), 5)
=======


    start_time = pygame.time.get_ticks()  # Record the start time
    last_speed_increase_time = start_time  # Track when the speed was last increased




    while running:
        screen.fill(background)  # Background fill




        # Get the current time elapsed
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - start_time




        # **Increase fall speed every 'speed_increase_interval' (5 seconds)**
        if current_time - last_speed_increase_time >= speed_increase_interval:
            fall_speed += 1  # Increase fall speed by 1
            last_speed_increase_time = current_time  # Update the last speed increase time


>>>>>>> aijish


        # Check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for tile in tiles:
<<<<<<< HEAD
                    if event.key == pygame.K_a and tile.x == 0 and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_s and tile.x == tile_width and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_d and tile.x == 2 * tile_width and tile.y + tile_height >= screen_height - 150:
=======
                    if event.key == pygame.K_1 and tile.x == 0 and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_2 and tile.x == tile_width and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_3 and tile.x == 2 * tile_width and tile.y + tile_height >= screen_height - 150:
>>>>>>> aijish
                        score += 1
                        tiles.remove(tile)
                        break


<<<<<<< HEAD
=======






>>>>>>> aijish
        # Add new tiles randomly
        if len(tiles) == 0 or tiles[-1].y > tile_height:
            x_pos = random.randint(0, 2) * tile_width
            new_tile = Tile(x_pos, -tile_height)
            tiles.append(new_tile)


<<<<<<< HEAD
=======






>>>>>>> aijish
        # Move and draw tiles
        for tile in tiles:
            tile.move()
            tile.draw()


<<<<<<< HEAD
=======






>>>>>>> aijish
        # Remove tiles that have fallen off the screen
        tiles = [tile for tile in tiles if tile.y < screen_height]


<<<<<<< HEAD
=======






>>>>>>> aijish
        # Draw the score
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))


<<<<<<< HEAD
=======






>>>>>>> aijish
        # Check for game over
        for tile in tiles:
            if tile.y + tile_height >= screen_height:
                running = False


<<<<<<< HEAD
        pygame.display.flip()


        # Frame rate
        clock.tick(60)


    # Game over screen
    game_over_text = font.render("Game Over!", True, (0, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.fill(BACKGROUND_COLOR)
=======






        pygame.display.flip()
        clock.tick(60)


    game_over_text = font.render("Game Lost!", True, (0, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.fill(background)
>>>>>>> aijish
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 50))
    screen.blit(final_score_text, (screen_width // 2 - 150, screen_height // 2 + 50))
    pygame.display.flip()


<<<<<<< HEAD
    # Pause for 3 seconds before quitting
    time.sleep(3)


    pygame.quit()


if __name__ == "__main__":
    run_game()
 



=======
    time.sleep(1)
    pygame.quit()
if __name__ == "__main__":
    run_game()
>>>>>>> aijish
