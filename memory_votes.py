

class MemoryVotes:

    def __init__(self):
        self.votes = {
            'yes': 0,
            'no': 0
        }

    def is_valid_vote(self, vote):
        return vote in self.votes

    def register_vote(self, vote):
        if self.is_valid_vote(vote):
            self.votes[vote] += 1

    def get_votes(self):
        return self.votes
