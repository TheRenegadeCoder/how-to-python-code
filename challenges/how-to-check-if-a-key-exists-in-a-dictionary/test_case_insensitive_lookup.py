import case_insensitive_lookup
from inspect import getmembers, isfunction


def test_case_insensitive_lookup_capital():
    dictionary = {
        "shrub": "a woody plant which is smaller than a tree and has several main stems arising at or near the ground."
    }
    for _, value in getmembers(case_insensitive_lookup, isfunction):
        assert value(dictionary, "Shrub") == dictionary["shrub"]
