import Structure
import Player
import Bot
import random


class Main:
    isPlayerTurn = False
    isBotTurn = False
    playerSymbol = ''
    botSymbol = ''

    def __init__(self, row, col, defVal, botname):
        self.board = Structure.Board(row, col, defVal)
        playerName = input('Enter your Name to continue\n')
        self.player = Player.Player(playerName)
        self.bot = Bot.Bot(botname)
        print('----------------------------\n')
        self.decideTurn()

    def decideTurn(self):
        t = random.randint(0, 1)
        if t == 0:
            print(f"{self.bot.name} will start first")
            self.isBotTurn = True
            self.botSymbol = 'O'
            self.playerSymbol = 'X'
        else:
            print(f"{self.player.name} will start first")
            self.isPlayerTurn = True
            self.playerSymbol = 'O'
            self.botSymbol = 'X'

    def startGame(self):
        while True:
            if self.isBotTurn:
                # Write your lines here
                self.bot.isMyTurn(self.botSymbol, self.board.returnAvailablePosition(), self.board)
                self.isBotTurn = False
                self.isPlayerTurn = True

            if self.isPlayerTurn:
                # Write your lines here
                print("Choose any number from 0 to 8")
                position = self.player.takePlayerInput(self.board)
                self.board.inputPlayerSelection(position, self.playerSymbol)
                self.isPlayerTurn = False
                self.isBotTurn = True

            if self.board.isWinCase(self.botSymbol if not self.isBotTurn else self.playerSymbol):
                if not self.isBotTurn:
                    print(f"{self.bot.name} is the winner...")
                    break
                else:
                    print(f"{self.player.name} is the winner...")
                    break
            else:
                if len(self.board.listOfAvailableIndexes) == 0:
                    print("It's a draw")
                    break


m = Main(3, 3, '_', 'Susy')
m.startGame()
