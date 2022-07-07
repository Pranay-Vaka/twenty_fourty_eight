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
                if self.board[y][x] == self.board[y][x - 1] and self.board[y][x] != "-" and [y][x] not in coords:
                    coords.append([x - 1, y])
        
        for i in coords:
            self.board[i[1]][i[0] + 1] = "-"
            self.board[i[1]][i[0]] *= 2

    
    def right(self):
        coords = []
        for y in range(0, 3):
            for x in range(0, 2):
                if self.board[y][x] == self.board[y][x + 1] and self.board[y][x] != "-" and [y, x] not in coords:
                    coords.append([x + 1, y])

        for i in coords:
            self.board[i[1]][i[0] - 1] = "-"
            self.board[i[1]][i[0]] *= 2
    
    def up(self):
        coords = []
        for y in range(1, 3):
            for x in range(0 ,3):
                if self.board[y][x] == self.board[y + 1][x] and self.board[y][x] != "-" and [y, x] not in coords:
                    coords.append([y + 1, x])

        for i in coords:
            self.board[i[1] - 1][i[0]] = "-"
            self.board[i[1]][i[0]] *= 2

    def down(self):
        pass

    