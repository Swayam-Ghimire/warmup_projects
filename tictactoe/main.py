# TicTacToe Game
from board import Board
from player import HumanPlayer, ComputerPlayer, AIPlayer
if __name__ == '__main__':
    game = Board()
    x_player = ComputerPlayer('X')
    o_player = AIPlayer('O')
    game.play(game, x_player, o_player)
    print('')



