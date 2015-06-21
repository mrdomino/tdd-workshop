import unittest
import leaderboard

class TestLeaderboard(unittest.TestCase):
    def test_empty(self):
        lb = leaderboard.Leaderboard()
        self.assertEqual(0, len(lb.leaders()))

    def test_has_one_leader(self):
        lb = leaderboard.Leaderboard()
        lb.track_score(5, object())
        self.assertEqual(1, len(lb.leaders()))
