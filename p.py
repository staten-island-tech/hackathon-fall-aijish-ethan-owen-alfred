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
