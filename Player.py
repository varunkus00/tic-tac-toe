import Structure


class Player(Structure.Board):
    playerInput = 0

    def __init__(self, player1):
        self.name = player1
        print('Player name is ' + self.name)

    def decideTurn(self):
        print(f"{self.name}'s turn first...")

    def takePlayerInput(self, board=Structure.Board()):
        self.playerInput = input()
        if not int(self.playerInput) in board.listOfAvailableIndexes:
            self.takePlayerInput()
        print(f"{self.name} chose Position - {self.playerInput}")
        return self.playerInput


