import solutions
from inspect import getmembers, isfunction


def test_capitalize_all_lowercase():
    for _, value in getmembers(solutions, isfunction):
        assert value("deku") == "Deku"


def test_capitalize_no_alphabet():
    for _, value in getmembers(solutions, isfunction):
        assert value("1234") == "1234"


def test_capitalize_all_caps():
    for _, value in getmembers(solutions, isfunction):
        assert value("TSUYU") == "Tsuyu"
