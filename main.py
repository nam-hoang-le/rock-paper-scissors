import players
from bots.mrugesh import mrugesh
from bots.abbey import abbey 
from bots.quincy import quincy
from bots.kris import kris 
from game import human, random_player, play
from players.player import player
from unittest import main

# Play interactively
#play(human, abbey, 20, verbose=True)


# Playground with bots
play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)



# Uncomment line below to run unit tests automatically
#main(module='test_module', exit=False)