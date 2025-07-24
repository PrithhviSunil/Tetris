import pygame
from shapes import Shapes_list, Colours_list
import random
from tetromino import Tetromino

pygame.init()

# Set up display
WIDTH, HEIGHT = 200, 400
WHITE = (255, 255,255)
BLACK = (0,0,0)

#set up timers
flag = 0
fall_speed = 1000 #1 second
drop = pygame.time.get_ticks()

#create a board
Board_width = 10
Board_height = 20
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


#get shape and its corresponding colour
Shape = random.choice(Shapes_list)
index = Shapes_list.index(Shape)
colour = Colours_list[index]
tetromino = Tetromino(Shape, colour)

#drawing each piece
def draw_piece():
    block_size = 20
    current_shape = tetromino.shape[tetromino.rotation]
    for row in range(4):
        for column in range(4):
            if current_shape[row][column]==1:
                x = (tetromino.x + column)*block_size
                y = (tetromino.y + row)*block_size
                rectangle = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(Screen, tetromino.colour,rectangle)


   



# Main loop
game = True
while game:
    Screen.fill(BLACK)
    #get time and move the piece down 1 row every second
    current = pygame.time.get_ticks()
    if current - flag > fall_speed:
        
        if not tetromino.landed(board):
            tetromino.move_down()
        else:
            tetromino.lockPieceOnBoard(board)
        
        #spawn new
            Shape = random.choice(Shapes_list)
            index = Shapes_list.index(Shape)
            colour = Colours_list[index]
            tetromino = Tetromino(Shape, colour)
        
        flag = current
    #draw grid and piece 
    draw_grid()
    draw_piece()
    pygame.display.flip() #refresh window 
    for event in pygame.event.get():
        #piece movement logic
        if not tetromino.landed(board):
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  
                    tetromino.move_left()
                elif event.key == pygame.K_RIGHT:  
                    tetromino.move_right()
                elif event.key == pygame.K_DOWN:
                    tetromino.move_down()    
                elif event.key == pygame.K_UP:
                    tetromino.rotate()
        #closing
        if event.type == pygame.QUIT:
            game = False
pygame.quit()