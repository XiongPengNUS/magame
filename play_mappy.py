import pygame
import sys
import os
from numpy import random


def play(maze, func):
    """The function plays the 'mappy' game.

    Parameters
    ----------
    maze: a two-dimensional nested list containing the information 
        of a 10*10 maze.
    func: a user-defined function to control the move of the mouse
    """
    
    pygame.display.init()
    pygame.font.init()
    
    dirt = os.path.dirname(__file__)
    
    display_width = 750
    display_height = 750

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Mappy in Maze')

    black = (0, 0, 0)
    yellow = (255, 255, 0)
    game_display.fill(black)

    clock = pygame.time.Clock()

    mouse = pygame.image.load(os.path.join(dirt, 'icons', 'mouse.png'))
    mouse = pygame.transform.scale(mouse, (50, 50))
    brick = pygame.image.load(os.path.join(dirt, 'icons', 'brick.png'))
    brick = pygame.transform.scale(brick, (50, 50))
    cat_names = [os.path.join(dirt, 'icons', 'meowky1.png'), 
                 os.path.join(dirt, 'icons', 'meowky2.png')]
    cat = pygame.image.load(cat_names[round(random.rand())])
    cat = pygame.transform.scale(cat, (50, 50))
    
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
                elif maze[i][j] == -1:
                    game_display.blit(cat, (125 + j*50, 125 + i*50))
                game_display.blit(brick, (125 + j*50, 75))
                game_display.blit(brick, (125 + j*50, row*50 + 125))
    
    def draw_mouse(position):            
        game_display.blit(mouse,
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
                if maze[y][x] == 0:
                    position = x, y
                elif maze[y][x] == -1:
                    win = True
            
            game_display.fill(black)
            draw_maze(maze)
            draw_mouse(position)
            
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
