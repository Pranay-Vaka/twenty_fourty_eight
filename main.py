import random

class Board():
    
    def __init__(self):
        self.alive = True
        self.board = [["-" for i in range(4)] for i in range(4)]

    def peek_board(self):
        for row in self.board:
            print(row)

    def is_alive(self):
        pass
        
    def left(self):
        coords = []
        for y in range(0, 3):
            for x in range(1, 3):
                if self.board[x][y] == self.board[x - 1][y] and self.board[x][y] != "-" and [x][y] not in coords:
                    coords.append([x - 1, y])

    def right(self):
        coords = []
        for y in range(0, 3):
            for x in range(0, 2):
                if self.board[x][y] == self.board[x + 1][y] and self.board[x][y] != "-" and [x, y] not in coords:
                    coords.append([x + 1, y])

        for i in coords:
            if coords
    
    def up(self):
        pass

    def down(self):
        pass

    