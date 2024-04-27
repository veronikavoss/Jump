import pygame
import os

TITLE = 'Jump'
SCALE = 1
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1280 * SCALE, 720 * SCALE
GROUND_SIZE = GROUND_X, GROUND_Y = 40 * SCALE, 40 * SCALE
CHARACTER_SIZE = CHARACTER_X, CHARACTER_Y = 40 * SCALE, 80 * SCALE
FPS = 165

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(CURRENT_PATH, 'image')
MAP_PATH = os.path.join(CURRENT_PATH, 'map')