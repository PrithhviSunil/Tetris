from shapes import Shapes_list, Colours_list
import random

Board_width = 10
Board_height = 20


class Tetromino():
    def __init__(self, shape, colour):
        self.shape = shape 
        self.colour = colour
        self.rotation =0
        #starting position = at the top middle
        self.x = random.randint(2,4)
        self.y = 0
    
    #movement  
    def move_left(self):
        self.x -=1
        if not self.is_inWindow(self.x, self.y):
            self.x +=1
    def move_right(self):
        self.x +=1
        if not self.is_inWindow(self.x, self.y):
            self.x -=1
    def move_down(self):
        self.y +=1
        if not self.is_inWindow(self.x, self.y):
            self.y -=1
                           
    #handles rotations and checks boundaries
    def rotate(self):
        initial = self.rotation
        self.rotation = (self.rotation + 1) % len(self.shape)
        offset = [0,1,-1,2,-2] #checks for wall kicks (if rotated state is outside the board)
        for i in offset:
            if self.is_inWindow(self.x + i, self.y):
                self.x +=i
                return 
        self.rotation=initial
             
    def is_inWindow(self, x_pos, y_pos):
        shape = self.shape[self.rotation]
        for row in range(4):
            for column in range(4):
                if shape[row][column]:
                    x_cor = x_pos + column
                    y_cor = y_pos + row
                    if x_cor < 0 or x_cor >= Board_width or y_cor>=Board_height:
                        return False
        return True
    
    #land the tetromino on the board
    def lockPieceOnBoard(self, board):
        shape = self.shape[self.rotation]
        for row in range(4):
            for column in range(4):
                value = shape[row][column]
                if value:
                    x_cor = column + self.x
                    y_cor = row + self.y
                    if 0<=y_cor<Board_height:
                        board[y_cor][x_cor]= Shapes_list.index(self.shape)+1
    
    def landed(self, board):
        shape = self.shape[self.rotation]
        for row in range(4):
            for column in range(4):
                value = shape[row][column]
                if value:
                    x_cor = column + self.x
                    y_cor = row + self.y +1
                    if y_cor >= Board_height or board[y_cor][x_cor] != 0:
                        return True
        return False





        
