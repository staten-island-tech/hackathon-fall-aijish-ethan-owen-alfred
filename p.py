import pygame
import random
import time

pygame.init()
screen_width = 300
screen_height = 400
tile_width = 100
tile_height = 50
fall_speed = 7

tiles = (0, 0, 0) #black
background = (255, 105, 180) #hot pink

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Music Squares')

pygame.font.SysFont("Comic Sans", 48)

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, tile_width, tile_height)

    def move(self):
        self.y += fall_speed
        self.rect.y = self.y

    def draw(self, is_pressed=False):
        color = (0, 200, 0) if is_pressed else tiles
        pygame.draw.rect(screen, color, self.rect, border_radius=10)