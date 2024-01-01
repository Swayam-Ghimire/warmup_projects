# TicTacToe Game
from board import Board
from player import HumanPlayer, ComputerPlayer
game = Board()
print("Below there is index for every box you should type.")
print('')
game.draw_num()
x_player = HumanPlayer('X')
o_player = ComputerPlayer('O')
game.play(game, x_player, o_player)
