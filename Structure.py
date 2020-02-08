class Board:
    gameBoard = [[]]
    __boardCols = 0
    __boardRows = 0
    playerCol = 0
    playerRow = 0
    listOfAvailableIndexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, cols=0, rows=0, defVal=''):
        if cols == 0 and rows == 0 and defVal == '':
            pass
        else:
            self.boardCols = cols
            self.boardRows = rows
            self.gameBoard = [[defVal for j in range(cols)] for i in range(rows)]
            print('Game Board created successfully...')

    def Board(self):
        for i in self.gameBoard:
            count = 0
            for j in i:
                if count < 2:
                    print(j, end='  |')
                else:
                    print(j)
                count += 1
            #print('\n')

    def inputPlayerSelection(self, position, value):
        self.decodePosition(position)
        self.gameBoard[self.playerRow][self.playerCol] = value
        self.listOfAvailableIndexes.remove(int(position))
        self.Board()

    def decodePosition(self, position):
        totallen = 9
        for i in range(totallen):
            if i == int(position):
                if i == 0 or i == 3 or i == 6:
                    self.playerCol = 0
                if i == 1 or i == 4 or i == 7:
                    self.playerCol = 1
                if i == 2 or i == 5 or i == 8:
                    self.playerCol = 2
                if i == 0 or i == 1 or i == 2:
                    self.playerRow = 0
                if i == 3 or i == 4 or i == 5:
                    self.playerRow = 1
                if i == 6 or i == 7 or i == 8:
                    self.playerRow = 2
            else:
                pass

    def isWinCase(self, playerSelection):
        if self.gameBoard[0][0] == self.gameBoard[1][0] == self.gameBoard[2][0] == playerSelection:
            return True
        if self.gameBoard[0][1] == self.gameBoard[1][1] == self.gameBoard[2][1] == playerSelection:
            return True
        if self.gameBoard[0][2] == self.gameBoard[1][2] == self.gameBoard[2][2] == playerSelection:
            return True
        if self.gameBoard[0][0] == self.gameBoard[0][1] == self.gameBoard[0][2] == playerSelection:
            return True
        if self.gameBoard[1][0] == self.gameBoard[1][1] == self.gameBoard[1][2] == playerSelection:
            return True
        if self.gameBoard[2][0] == self.gameBoard[2][1] == self.gameBoard[2][2] == playerSelection:
            return True
        if self.gameBoard[0][0] == self.gameBoard[1][1] == self.gameBoard[2][2] == playerSelection:
            return True
        if self.gameBoard[2][0] == self.gameBoard[1][1] == self.gameBoard[0][2] == playerSelection:
            return True

        return False

    def returnAvailablePosition(self):
        return self.listOfAvailableIndexes
