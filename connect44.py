import numpy as np

class Connect4:

    def __init__(self):
        self.board = np.zeros((7, 6))

    def displayBoard(self):
        print(self.board)

    def input(self, marker):    #marker is 1 for X or 2 for O
        inputting = True
        while(inputting):
            col = input('Player '+str(marker)+" Pick a column 1-6: ")
            try:
                col = int(col) - 1
                inputting = False
            except ValueError:
                print('Please enter a number')
                continue

        for i in range(0,7):
            if self.board[6-i][col] == 0:
                self.board[6-i][col] = marker
                break
            elif 6-i == 1:
                print('Column full')
            else:
                continue

    def clearBoard(self):
        self.board = np.zeros((7,6))

#checks not working yet
    def checkVertLines(self, marker):
        # Checkin lines
        for j in range(0, 6):
            for i in range(0, 3):
                if self.board[i][j] == marker and self.board[i+1][j] == marker and self.board[i+2][j] == marker and self.board[i+3][j] == marker:
                    return True
        return False
                
    def checkHorizLines(self, marker):
        size = self.board.shape #(rows, cols)
        for i in range(0, size[0]):
            for j in range(0,3 ):
                if self.board[i][j] == marker and self.board[i+1][j] == marker and self.board[i+2][j] == marker and self.board[i+3][j] == marker:
                    return True
        return False

c = Connect4()
c.input(1)
c.input(1)
c.input(1)
c.input(1)
c.input(1)
c.input(1)
c.input(1)
c.input(1)
