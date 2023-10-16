import pygame
import os

# Constants
CELL_SIZE = 30
WIDTH_BLOCKS = 10
HEIGHT_BLOCKS = 20
BUFFER_ZONE = 2
WIDTH = CELL_SIZE * WIDTH_BLOCKS
HEIGHT = CELL_SIZE * HEIGHT_BLOCKS + CELL_SIZE * BUFFER_ZONE
MAX_FPS = 60
OFFSET_X = CELL_SIZE * 4
OFFSET_Y = CELL_SIZE * 2
MAIN_COLOR = pygame.Color(25,26,37)

TETROMINOES = {'T' : [(-1,0),(0,0),(0,-1),(1,0)],
               'I' : [(-2,0),(-1,0),(0,0),(1,0)],
               'J' : [(-1,0),(0,0),(0,-1),(0,-2)],
               'O' : [(0,-1),(-1,-1),(-1,0),(0,0)],
               'L' : [(0,0),(-1,0),(-1,-1),(-1,-2)]}

class Tetris:
    def __init__(self):
        pass

    def draw_grid(self):
        for x in range(WIDTH_BLOCKS):
            for y in range(HEIGHT_BLOCKS + BUFFER_ZONE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (0,0,0), rect, 1)

class Block:
    pass

class Tetromino:
    def __init__(self):
        self.type = 'L'
        

    def draw_tetromino(self):
        for pos in TETROMINOES[self.type]:
            rect = pygame.Rect(pos[0] * CELL_SIZE + OFFSET_X, pos[1] * CELL_SIZE + OFFSET_Y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0,255,0), rect)


# Main functions
def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def update():
    pygame.display.flip()
    clock.tick(MAX_FPS)


dimensions = (WIDTH, HEIGHT) 
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
tetromino = Tetromino()
tetris = Tetris()

while True:
    event_handler()
    screen.fill(MAIN_COLOR)
    tetris.draw_grid()
    tetromino.draw_tetromino()
    update()