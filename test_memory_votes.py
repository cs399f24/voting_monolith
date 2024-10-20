from memory_votes import MemoryVotes


def test_new_instance_has_no_votes():
    votes = MemoryVotes()
    assert votes.get_votes() == {'yes': 0, 'no': 0}


def test_can_register_vote():
    votes = MemoryVotes()
    votes.register_vote('yes')
    assert votes.get_votes() == {'yes': 1, 'no': 0}
    votes.register_vote('no')
    assert votes.get_votes() == {'yes': 1, 'no': 1}


def test_invalid_vote():
    votes = MemoryVotes()
    assert not votes.is_valid_vote('invalid')
    assert votes.is_valid_vote('yes')
    assert votes.is_valid_vote('no')


def test_invalid_vote_not_registered():
    votes = MemoryVotes()
    votes.register_vote('invalid')
    assert votes.get_votes() == {'yes': 0, 'no': 0}