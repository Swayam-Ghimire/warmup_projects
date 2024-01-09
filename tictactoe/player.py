import random
import math


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
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


class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            box = random.choice(game.available_moves())
        else:
            box = self.minimax(game, self.letter)['position']

        return box

    def minimax(self, game, player):
        # determine the max player
        max_player = self.letter
        min_player = 'O' if player == 'X' else 'X'
        # first we want to check if the previous move is a winner
        if game.current_winner == min_player:
            return {'position': None,
                    'score': 1 * (game.num_empty_squares() + 1) if min_player == max_player else -1 * (
                            game.num_empty_squares() + 1)}
        # if not winner we check whether it is a draw
        elif not game.empty_squares():
            return {'position': None, 'score': 0}
        # initialize the best move
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # position and score for max player
        else:
            best = {'position': None, 'score': math.inf}  # position and score for min player
        for possible_move in game.available_moves():
            # make a move and evaluate scores for every possible outcomes
            game.make_move(possible_move, player)
            sim_score = self.minimax(game, min_player)  # simulate a game after making that move

            # undo move
            game.board[possible_move] = ' '
            game.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:
                # checks for the best scores ie utility values for  max player
                # update if the score is maximum
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                # checks for the best score ie utility values for min player
                # update if the score is lower (minimize score)
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
