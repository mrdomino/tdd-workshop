class Leaderboard(object):
    def __init__(self, max=5):
        self._leaders = []
        self._max = max

    def leaders(self):
        return list(self._leaders)

    def track_score(self, score, obj):
        if len(self._leaders) < self._max:
            self._leaders.append(obj)

    def get_score(self, obj):
        return 5
