import unittest
import leaderboard

class TestLeaderboard(unittest.TestCase):
    def test_empty(self):
        it = leaderboard.Leaderboard()
        self.assertEqual(0, len(it.leaders()))
