import random
from board import Board

b = Board()


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self):
        flag = True
        box = None
        while flag:
            box = int(input(f'{self.letter} \'s turn (0-8):'))
            try:
                if box not in b.available_moves():
                    raise ValueError

                flag = False
            except ValueError:
                print("Invalid box!!")
        return box


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self):
        box = random.choice(b.available_moves())
        return box
