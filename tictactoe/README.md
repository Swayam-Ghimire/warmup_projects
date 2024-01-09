## Tictactoe Game with Minimax Algorithm
_This game is designed by using python where a human player,
computer player, or an AI player can play between each other.
This code shows the gameplay between an AI player and a Human
player. We can modify this code to show gameplay between
human player and computer player or computer player and AI Player._

### Files
* main.py is the main file where the code is run.
* player.py is the file that defines all Players classes.
* board.py is the file that defines Board class which contains game functions.

### Minimax Algorithm
_This algorithm is implemented on AIPlayer Class from player.py.
It is the algorithm used to reduce the chance of loss of the max player
in a two players game like chess, tictactoe, etc._

_In this code the AIPlayer gives utility value to all the 
possible outcome of the game. It selects the path where it can
get maximum utility value. According to the maximum utility value
the move index is returned or the box or position of the 
optimal move is returned._

**The utility value is determined by utility function.**
* For max player win: 1 * (number of empty boxes left + 1)
* For min player win: -1 * (number of empty boxes left + 1)
* For a tie: 0
