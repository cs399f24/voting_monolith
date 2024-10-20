from redis_votes import RedisVotes
from fakeredis import FakeStrictRedis


def test_new_instance_has_no_votes():
    redis_server = FakeStrictRedis()
    votes = RedisVotes(redis_server)
    assert votes.get_votes() == {'yes': 0, 'no': 0}


def test_can_register_vote():
    redis_server = FakeStrictRedis()
    votes = RedisVotes(redis_server)
    votes.register_vote('yes')
    assert votes.get_votes() == {'yes': 1, 'no': 0}
    votes.register_vote('no')
    assert votes.get_votes() == {'yes': 1, 'no': 1}


def test_invalid_vote():
    redis_server = FakeStrictRedis()
    votes = RedisVotes(redis_server)
    assert not votes.is_valid_vote('invalid')
    assert votes.is_valid_vote('yes')
    assert votes.is_valid_vote('no')


def test_invalid_vote_not_registered():
    redis_server = FakeStrictRedis()
    votes = RedisVotes(redis_server)
    votes.register_vote('invalid')
    assert votes.get_votes() == {'yes': 0, 'no': 0}