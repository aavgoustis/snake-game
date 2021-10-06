#!/usr/bin/env python3

import pygame
import time
import random

snake_speed = 10

# Window size
window_x = 720
window_y = 480

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initialise pygame
pygame.init()

# initialise window
pygame.display.set_caption('Shitty snake game by aavgoustis')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS
fps = pygame.time.Clock()

# default position
snake_position = [100, 50]

# first 4 blocks
# body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# set default snake direction (right)
direction = 'RIGHT'
change_to = direction

## Scoreboard
# initial score
score = 0

# scoreboard function
def show_score(choice, color, font, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the surface object
    score_surface = score_font.render('Score: ' + str(score), True, color)

    # create rectangular object for the text
    score_rect = score_surface.get_rect()

    # displaying the text
    game_window.blit(score_surface, score_rect)

def game_over():

    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # text surface for the text to be drawn on
    game_over_surface = my_font.render('Your score is: ' + str(score), True, red)

    # rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # draw text on the screen using blit()
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 sec quit the program
    time.sleep(1)

    # deactivate pygame lib
    pygame.quit()

    # quit the program
    quit()

# Main
while True:

    # key listeners
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_d:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                game_over()

    # if 2 kes are pressed at once, the snake won't move in 2 directions at once
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # snake growing mechanism if snake and fruit collide, increase score by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10
        ))

    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10
    ))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # display score continuously
    show_score(1, white, 'times new roman', 20)

    # refresh game screen
    pygame.display.update()

    # FPS
    fps.tick(snake_speed)
