import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        flag = True
        box = None
        while flag:
            try:
                box = int(input(f'{self.letter} \'s turn (0-8):'))
                if box not in game.available_moves():
                    raise ValueError

                flag = False
            except ValueError:
                print("Invalid box!!")
        return box


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        box = random.choice(game.available_moves())
        return box
