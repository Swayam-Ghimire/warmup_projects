import random


def play():
    player = input("Enter 'r' for Rock, 's' for scissors, 'p' for paper: ").lower()
    opponent = random.choice(['r', 'p', 's'])
    print(f'Player:{player} Opponent:{opponent}')
    if player == opponent:
        return "It\'s a tie!!!"
    if win(player, opponent):
        return 'Player wins'
    return 'Opponent wins'


def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True


print(play())
