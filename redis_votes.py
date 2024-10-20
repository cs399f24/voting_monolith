

class RedisVotes:

    def __init__(self, redis):
        self.redis = redis

    def is_valid_vote(self, vote):
        return vote in ['yes', 'no']

    def register_vote(self, vote):
        if self.is_valid_vote(vote):
            self.redis.incr(vote)

    def get_votes(self):
        yes = self.redis.get('yes')
        if not yes:
            yes = 0
        no = self.redis.get('no')
        if not no:
            no = 0
        return {'yes': int(yes), 'no': int(no)}



