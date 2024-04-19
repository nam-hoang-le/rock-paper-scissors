# Rock, Paper, Scissors Game

Welcome to the Rock, Paper, Scissors (RPS) game! In this game, I developed a program to play the classic game of Rock, Paper, Scissors against four different bots. The goal is to win at the maximum of the games against each bot.

## Instructions

In the player, you'll find a file named player.py. This contains a function takes one argument, a string describing the last move of the opponent ("R" for Rock, "P" for Paper, or "S" for Scissors), and returns a string representing the next move for your program to play.

For the first game in each match, the player function will receive an empty string as its argument since there is no previous play to consider.

To defeat all four opponents, I developed multiple strategies that adapt depending on the opponent's plays.

## Development


main.py imports the game function and bots from RPS_game.py.

To test your code, use the play function. It takes four arguments:

Two players to play against each other (these are actually functions).
The number of games to play in the match.
An optional argument to see a log of each game. Set it to True to see these messages.


```python
play(player, quincy, 1000, verbose=True)
```

Click the "run" button, and main.py will execute the game.

## Testing







