import solutions
from inspect import getmembers, isfunction


def test_capitalize_all_lowercase():
    for _, value in getmembers(solutions, isfunction):
        assert value("deku") == "Deku"
