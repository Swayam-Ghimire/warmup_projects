class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 9 elements for board
        self.current_winner = None

    def draw(self):
        """This function is for making the tictactoe board"""
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print(' | '.join(row))

    def available_moves(self):
        """Determines the available moves to play"""
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def first_turn(self):
        """Determine the first move"""
        letter = 'X' if self.current_winner == 'X' else 'O'
        return letter

    def make_move(self, box, letter):
        if self.board[box] == ' ':
            self.board[box] = letter
            if self.winner(box, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, box, letter):
        # Row wise winner
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            if letter in row[0] and letter in row[1] and letter in row[2]:
                return True

        # Column wise winner

        return False

    @staticmethod
    def draw_num():
        num_board = [[str(j) for j in range(i * 3, (i + 1) * 3)] for i in range(3)]
        for row in num_board:
            print(' | '.join(row))
        print('')

    def play(self, game, x_player, o_player):
        letter = self.first_turn()
        self.draw()
        while ' ' in self.board:
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
                exit()
            letter = 'O' if letter == 'X' else 'X'

        print("It's a tie!!")
