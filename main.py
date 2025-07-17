import pygame
from shapes import Shapes_list, Colours_list
pygame.init()

# Set up display
WIDTH, HEIGHT = 200, 400
WHITE = (255, 255,255)
BLACK = (0,0,0)

#create a board
Board_width = 20
Board_height = 40
board = [[0 for j in range(Board_width)] for i in range(Board_height)]

Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


#Drawing Grid 
def draw_grid():
    block_size = 20
    for i in range(Board_height):
        for j in range(Board_width):
            #get pixel coordinates for each block
            x = j*block_size
            y = i*block_size
            #draw rectangles
            rectangle = pygame.Rect(x, y, block_size, block_size)
            if board[i][j]!=0: #get colours
                col_index = board[i][j]-1
                colour = Colours_list[col_index]
                pygame.draw.rect(Screen,colour,rectangle)
            pygame.draw.rect(Screen, WHITE, rectangle, 1)

#Tetromino Class
def tetromino():
    pass

# Main loop
running = True
while running:
    Screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()