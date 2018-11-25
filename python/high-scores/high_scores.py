class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores.pop()

    def highest(self):
        return max(self.scores)

    def top(self):
            return sorted(self.scores, reverse=True)[0:3]

    def report(self):
        stringbest = "Your latest score was {}. That's your personal best!"

        stringnotbest = "Your latest score was {}. That's {} short of your personal best!"
        highest = self.highest()
        latest = self.latest()

        if highest > latest:
            resultstring = stringnotbest.format(latest, (highest - latest))
        elif highest <= latest:
            resultstring = stringbest.format(latest)
        return resultstring
