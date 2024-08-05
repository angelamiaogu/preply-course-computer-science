
import pygame
class Snake(object):
    def __init__(self,snake_list=[[200, 300],[190, 300],[180, 300]], block_size=10, speed=5,window = None,display_width=600,display_height=400):

        self.window = window
        self.snake_list = snake_list
        self.block_size = block_size
        self.speed = speed
        self.snake_position = 'right'
        self.green = (0, 255, 0)
        self.display_width = display_width
        self.display_height = display_height

     # Draw snake
    def draw_snake(self):
        for pos in self.snake_list:
            pygame.draw.rect(self.window, self.green, [pos[0], pos[1], self.block_size, self.block_size])

    def move_snake(self):
        head = self.snake_list[-1].copy()
        if self.snake_position == 'left':
            head[0] -= self.block_size
        elif self.snake_position == 'right':
            head[0] += self.block_size
        elif self.snake_position == 'up':
            head[1] -= self.block_size
        elif self.snake_position == 'down':
            head[1] += self.block_size
            
        
        self.snake_list.append(head)
        self.snake_list.pop(0)
    
    def set_position(self, snake_position):
        self.snake_position = snake_position



   

    def update_snake(self):
        self.snake_list.append(self.snake_list[-1].copy())

    def get_snake_list(self):
        return self.snake_list


    def detect_collision(self):
        if self.snake_list[-1][0] >= self.display_width or self.snake_list[-1][0] < 0 or self.snake_list[-1][1] >= self.display_height or self.snake_list[-1][1] < 0:
            print("Game Over!!")
            return False
        else:
            return True
        
    def self_collision(self):
        if self.snake_list[-1] in self.snake_list[2:-2]:
            print("Game Over!!")
            return False
        else:
            return True