import pygame
import sys
from numpy import random
import numpy as np
from copy import deepcopy
import os


def play(maze, func):
    """The function plays the 'mappy' game.

    Parameters
    ----------
    maze: a two-dimensional nested list containing the information 
        of a 10*10 maze.
    func: a user-defined function to control the move of the pac man
    """
    maze = [[item if item != -1 else 0 for item in line] for line in maze]
    maze[0][0] = -1
    dot_count = (np.array(maze) == 0).sum()
    
    dirt = os.path.dirname(__file__)
    
    pygame.display.init()
    pygame.font.init()

    display_width = 750
    display_height = 750

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Pac-man in Maze')

    black = (0, 0, 0)
    yellow = (255, 255, 0)
    game_display.fill(black)

    clock = pygame.time.Clock()
    brick = pygame.image.load(os.path.join(dirt, 'icons', 'brick.png'))
    brick = pygame.transform.scale(brick, (50, 50))
    dot = pygame.image.load(os.path.join(dirt, 'icons', 'dot.png'))
    dot = pygame.transform.scale(dot, (50, 50))
    
    row = len(maze)
    column = len(maze)
    
    def draw_maze(maze):
        game_display.blit(brick, (75, 75))
        game_display.blit(brick, (75, row*50 + 125))
        game_display.blit(brick, (column*50 + 125, row*50 + 125))
        game_display.blit(brick, (column*50 + 125, 75))
        for i in range(row):
            game_display.blit(brick, (75, 125 + i*50))
            game_display.blit(brick, (column*50 + 125, 125 + i*50))
            for j in range(column):
                if maze[i][j] == 1:
                    game_display.blit(brick, (125 + j*50, 125 + i*50))
                elif maze[i][j] == 0:
                    game_display.blit(dot, (125 + j*50, 125 + i*50))
                game_display.blit(brick, (125 + j*50, 75))
                game_display.blit(brick, (125 + j*50, row*50 + 125))
    
    def draw_pac(position):            
        game_display.blit(pac,
                          (125 + position[0]*50, 125 + position[1]*50))
    
    run = True
    x_change, y_change = 0, 0
    start = 0, 0
    position = start
    win = False
    count = 0
    memory = None
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not win:
            new_move, memory = func(maze, position, memory)
            x_change, y_change = new_move
            #x_change, y_change = func(maze, position, (x_change, y_change))
            if abs(x_change) + abs(y_change) != 1 and \
               abs(x_change) + abs(y_change) != 0:
                raise ValueError('Invalid move!')
        
            x = min(position[0] + x_change, column - 1)
            x = max(x, 0)
            y = min(position[1] + y_change, row - 1)
            y = max(y, 0)
            if x_change != 0 or y_change != 0:
                """
                if maze[y][x] == 0:
                    position = x, y
                elif maze[y][x] == -1:
                    win = True
                """
                if maze[y][x] == 0:
                    position = x, y
                    maze[y][x] = -1
                    dot_count -= 1
                elif maze[y][x] == -1:
                    position = x, y
                
                if dot_count == 0:
                    win = True
            
            game_display.fill(black)
            draw_maze(maze)
            
            if x_change == 0 and y_change == -1:
                pac = pygame.image.load(os.path.join(dirt, 'icons', 'pacman_up.png'))
            elif x_change == 0 and y_change == 1:
                pac = pygame.image.load(os.path.join(dirt, 'icons', 'pacman_down.png'))
            elif x_change == 1 and y_change == 0:
                pac = pygame.image.load(os.path.join(dirt, 'icons', 'pacman_right.png'))
            else:
                pac = pygame.image.load(os.path.join(dirt, 'icons', 'pacman_left.png'))
            pac = pygame.transform.scale(pac, (50, 50))
            
            draw_pac(position)
            
            count += 1
        else:
            game_display.fill(black)
            font = pygame.font.Font('freesansbold.ttf', 64)
            text = font.render('You Win', True, yellow)
            text_rect = text.get_rect().center = (235, 325)
            game_display.blit(text, text_rect)
    
        pygame.display.update()
        clock.tick(4)

    pygame.display.quit()
    pygame.font.quit()
    pygame.quit()
    try:
        sys.exit(0)
    except SystemExit:
        print('You took {0} steps'.format(count))
