import pygame
import random
import time
pygame.init()

screen_width = 300
screen_height = 400
tile_width = 100
tile_height = 50
fall_speed = 2
speed_increase_interval = 5000

TILE_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 105, 180)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Music Squares')

font = pygame.font.Font(None, 48)

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

def run_game():
    global fall_speed
   
    tiles = []
    score = 0
    running = True
    clock = pygame.time.Clock()


    start_time = pygame.time.get_ticks()
    last_speed_increase_time = start_time 


    while running:
        screen.fill(BACKGROUND_COLOR)
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - start_time

        if current_time - last_speed_increase_time >= speed_increase_interval:
            fall_speed += 1
            last_speed_increase_time = current_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for tile in tiles:
                    if event.key == pygame.K_1 and tile.x == 0 and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_2 and tile.x == tile_width and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break
                    elif event.key == pygame.K_3 and tile.x == 2 * tile_width and tile.y + tile_height >= screen_height - 150:
                        score += 1
                        tiles.remove(tile)
                        break


        if len(tiles) == 0 or tiles[-1].y > tile_height:
            x_pos = random.randint(0, 2) * tile_width
            new_tile = Tile(x_pos, -tile_height)
            tiles.append(new_tile)

        for tile in tiles:
            tile.move()
            tile.draw()

        tiles = [tile for tile in tiles if tile.y < screen_height]

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        for tile in tiles:
            if tile.y + tile_height >= screen_height:
                running = False
        pygame.display.flip()

        clock.tick(60)

    game_over_text = font.render("Game Over!", True, (0, 0, 0))
    final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    screen.fill(BACKGROUND_COLOR)
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 50))
    screen.blit(final_score_text, (screen_width // 2 - 150, screen_height // 2 + 50))
    pygame.display.flip()

    time.sleep(3)
    pygame.quit()

if __name__ == "__main__":
    run_game()