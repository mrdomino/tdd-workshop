class Leaderboard(object):
    def __init__(self):
        self._x = 0

    def leaders(self):
        return [object() for _ in range(self._x)]

    def track_score(self, score, obj):
        self._x = self._x + 1
