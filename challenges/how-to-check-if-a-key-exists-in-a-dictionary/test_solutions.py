import solutions
from inspect import getmembers, isfunction


def test_case_insensitive_lookup_capital():
    dictionary = {
        "shrub": "a woody plant which is smaller than a tree and has several main stems arising at or near the ground."
    }
    for _, value in getmembers(solutions, isfunction):
        assert value(dictionary, "Shrub") == dictionary["shrub"]
