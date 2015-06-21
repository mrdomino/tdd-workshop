class Leaderboard(object):
    def __init__(self, max=None):
        self._leaders = []

    def leaders(self):
        return self._leaders

    def track_score(self, score, obj):
        self._leaders.append(obj)
