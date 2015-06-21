import unittest
import leaderboard

class TestLeaderboard(unittest.TestCase):
    def test_empty(self):
        it = leaderboard.Leaderboard()
        self.assertEqual(0, len(it.leaders()))

    def test_has_one_leader(self):
        it = leaderboard.Leaderboard()
        it.track_score(5, object())
        self.assertEqual(1, len(it.leaders()))

    def test_returns_leader_object(self):
        it = leaderboard.Leaderboard()
        bob = object()
        it.track_score(1, bob)
        self.assertEqual(bob, it.leaders()[0])
