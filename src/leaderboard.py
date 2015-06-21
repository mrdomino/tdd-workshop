class Leaderboard(object):
    def __init__(self):
        self.x = 0

    def leaders(self):
        return range(self.x)

    def track_score(self, score, obj):
        self.x = self.x + 1
