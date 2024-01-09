import time


class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 9 elements for board
        self.current_winner = None

    def draw(self):
        """This function is for making the tictactoe board"""
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('|', ' | '.join(row), '|')

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        """Determines the available moves to play"""
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def make_move(self, box, letter):
        if self.board[box] == ' ':
            self.board[box] = letter
            if self.winner(box, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, box, letter):
        # Row wise winner
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            # The all() function in Python returns True if all elements in a list are true (or if the list is empty).
            # If any element is False, it returns False
            if all([r == letter for r in row]):  # if letter in row[0] and letter in row[1] and letter in row[2]
                return True
        # Column wise winner
        col_idx = box % 3
        if all([column == letter for column in [self.board[col_idx + i * 3] for i in range(3)]]):
            return True

        # Diagonal wise winner
        diagonal_idx = [[0, 4, 8], [2, 4, 6]]
        for diagonal in diagonal_idx:
            diagonal1 = [self.board[d1] for d1 in diagonal]
            if all([d == letter for d in diagonal1]):
                return True
        return False

    @staticmethod
    def draw_num():
        num_board = [[str(j) for j in range(i * 3, (i + 1) * 3)] for i in range(3)]
        for row in num_board:
            print('|', ' | '.join(row), '|')
        print('')

    def play(self, game, x_player, o_player):
        letter = 'X'
        print("Below there is index for every box you should type.")
        print('')
        self.draw_num()
        while self.empty_squares():
            if letter == 'X':
                box = x_player.get_move(game)
            else:
                box = o_player.get_move(game)
            if self.make_move(box, letter):
                print(f'{letter} player made a move to box {box}')
                self.draw()
                print('')

            if self.current_winner in ['X', 'O']:
                print(f'{self.current_winner} wins the game!!!')
                return
            time.sleep(0.9)
            letter = 'O' if letter == 'X' else 'X'

        print("It's a tie!!")
