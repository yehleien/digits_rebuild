
class ScoreSystem:
    def __init__(self):
        self.total_score = 0
        self.rounds_played = 0

    def update_score(self, round_score):
        self.total_score += round_score
        self.rounds_played += 1

    def get_average_score(self):
        if self.rounds_played == 0:
            return 0
        return self.total_score / self.rounds_played

    def get_total_score(self):
        return self.total_score

    def reset_score(self):
        self.total_score = 0
        self.rounds_played = 0

