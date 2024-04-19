import unittest
from bots.mrugesh import mrugesh
from bots.abbey import abbey 
from bots.quincy import quincy
from bots.kris import kris 
from system.game import play
from players.player import player

class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("Testing game against quincy...")
        actual = play(player, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat quincy at least 60% of the time.')

    def test_player_vs_abbey(self):
        print("Testing game against abbey...")
        actual = play(player, abbey, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat abbey at least 60% of the time.')

    def test_player_vs_kris(self):
        print("Testing game against kris...")
        actual = play(player, kris, 1000) >= 60
        self.assertTrue(
            actual, 'Expected player to defeat kris at least 60% of the time.')

    def test_player_vs_mrugesh(self):
        print("Testing game against mrugesh...")
        actual = play(player, mrugesh, 1000) >= 60
        self.assertTrue(
            actual,
            'Expected player to defeat mrugesh at least 60% of the time.')


if __name__ == "__main__":
    unittest.main()
