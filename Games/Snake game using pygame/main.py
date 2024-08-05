import pygame
import time
import random
from snake import Snake
from food import Food
pygame.init()
 



        # Screen size
display_width = 1000
display_height = 800

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

block_size = 10
snake = Snake(block_size=block_size,  window=window, display_width=display_width, display_height=display_height)

food_x = 300
food_y = 200
food  = Food(food_x, food_y, block_size=block_size, display_width=display_width, display_height=display_height, window=window)
clock = pygame.time.Clock()

def detect_food_collision(snake_position_list, food_x, food_y):
    if snake_position_list[-1][0] == food_x and snake_position_list[-1][1] == food_y:
        # print("Yummy!!") food and snake
        food.update_food()
        food_x_updated = food.get_food_x()
        food_y_updated= food.get_food_y()
        snake.update_snake()

        return food_x_updated, food_y_updated
    else:
        return food_x, food_y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake.snake_position != 'right':
                    snake.set_position('left')
            elif event.key == pygame.K_RIGHT:
                if snake.snake_position != 'left':
                    snake.set_position('right')
            elif event.key == pygame.K_UP:
                if snake.snake_position != 'down':
                    snake.set_position('up')
            elif event.key == pygame.K_DOWN:
                if snake.snake_position != 'up':
                    snake.set_position('down')

    snake.move_snake()
    black = (0, 0, 0)
    window.fill(black)
    snake.draw_snake()
    food.draw_food(food_x, food_y)
    snake_position_list = snake.get_snake_list()
    
    food_x, food_y = detect_food_collision(snake_position_list, food_x, food_y)
    running = snake.detect_collision()
    #running = snake.self_collision()


    pygame.display.update()
    
    clock.tick(5)

pygame.quit()
