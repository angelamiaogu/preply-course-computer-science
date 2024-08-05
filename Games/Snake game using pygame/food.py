import random
import pygame
class Food(object):
    def __init__(self, x, y, block_size,display_width,display_height,window):
        self.block_size = block_size
        self.x = x
        self.y = y
        self.display_width = display_width
        self.display_height = display_height
        self.window = window
        self.draw_food(x, y)

    def draw_food(self, x, y):
        pygame.draw.rect(self.window, 'red', [x, y, self.block_size, self.block_size])

    def update_food(self):
        self.x = round(random.randrange(0, self.display_width - self.block_size) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.display_height - self.block_size) / 10.0) * 10.0
    def get_food_x(self):
        return self.x
    def get_food_y(self):
        return self.y
