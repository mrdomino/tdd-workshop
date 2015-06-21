class Leaderboard(object):
    def __init__(self, max=5):
        self._leaders = dict()
        self._max = max

    def leaders(self):
        return [k for k, v in self._leaders.items()]

    def track_score(self, score, obj):
        if len(self._leaders) < self._max:
            self._leaders[obj] = score

    def get_score(self, obj):
        return self._leaders[obj]
