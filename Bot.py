import Structure
import random


class Bot(Structure.Board):

    def __init__(self, name):
        self.name = name
        print('Bot name is ' + name)

    def isMyTurn(self, botSymbol, indexes=[], board=Structure.Board()):
        position = random.choice(indexes)
        print(f"{self.name} chose Position - {position}")
        board.inputPlayerSelection(position, botSymbol)
        return indexes
