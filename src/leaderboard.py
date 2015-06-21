class Leaderboard(object):
    def __init__(self, max=None):
        self._leaders = []
        self._max = max

    def leaders(self):
        return self._leaders

    def track_score(self, score, obj):
        if not self._max or len(self._leaders) < self._max:
            self._leaders.append(obj)
