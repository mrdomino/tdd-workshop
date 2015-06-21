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

    def test_returns_leader_object(self):
        lb = leaderboard.Leaderboard()
        bob = object()
        lb.track_score(1, bob)
        self.assertEqual(bob, lb.leaders()[0])

    def test_stores_up_to_max(self):
        lb = leaderboard.Leaderboard(max=5)
        for i in range(5):
            lb.track_score(2, object())
            self.assertEqual(i + 1, len(lb.leaders()))
