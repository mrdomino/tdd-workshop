import unittest
import leaderboard

class TestLeaderboard(unittest.TestCase):
    def test_empty(self):
        lb = leaderboard.Leaderboard()
        self.assertEqual(0, len(lb.leaders()))
