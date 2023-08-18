from print_joke import get_random_reaction


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert isinstance(reaction, str)# Replace False with a check that makes sure the reaction is a string type


def test_get_random_reaction_repeats():
    # Write a test that checks that multiple calls to get_random_reaction()
    reactions = {get_random_reaction() for _ in range(10)}

    # doesn't give you the same reaction every time
    assert len(reactions) > 1


# Come up with a test of your own and implement it here.
def test_reaction_length():
    reaction_length = 10
    assert len(get_random_reaction()) == reaction_length


if __name__ == "__main__":
    test_get_random_reaction_type()
    test_get_random_reaction_repeats()
    test_reaction_length()