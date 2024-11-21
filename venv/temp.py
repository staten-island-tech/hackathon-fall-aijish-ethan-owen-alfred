import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tile Run Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock for frame rate
clock = pygame.time.Clock()

# Background music
pygame.mixer.init()
pygame.mixer.music.load("toi.mp3")
pygame.mixer.music.play(-1)  # Loop indefinitely

# Player
player_size = 50
player_x = 100
player_y = HEIGHT - player_size
player_velocity = 0
gravity = 0.5

# Tiles
tile_width = 100
tile_height = 20
tile_gap = 300
tiles = []
for i in range(5):
    tile_x = random.randint(0, WIDTH - tile_width)
    tile_y = i * -tile_gap
    tiles.append(pygame.Rect(tile_x, tile_y, tile_width, tile_height))

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player mechanics
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_y == HEIGHT - player_size:  # Jump
        player_velocity = -10

    player_velocity += gravity
    player_y += player_velocity
    if player_y > HEIGHT - player_size:
        player_y = HEIGHT - player_size

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Tiles movement
    for tile in tiles:
        tile.y += 5
        if tile.y > HEIGHT:
            tile.y = random.randint(-tile_gap, 0)
            tile.x = random.randint(0, WIDTH - tile_width)

        pygame.draw.rect(screen, BLACK, tile)

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit pygame
pygame.quit()
