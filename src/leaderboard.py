class Leaderboard(object):
    def __init__(self, max=5):
        self._leaders = []
        self._max = max

    def leaders(self):
        return [x['obj'] for x in self._leaders]

    def track_score(self, score, obj):
        if len(self._leaders) < self._max:
            self._leaders.append({'score': score, 'obj': obj})

    def get_score(self, obj):
        for x in self._leaders:
            if x['obj'] == obj:
                return x['score']
