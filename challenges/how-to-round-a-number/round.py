"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-round-a-number-in-python/#challenge
"""

import math


def round_1(num: int):
    # Floor (round to -∞)
    return math.floor(num)


def round_2(num: int):
    # Ceiling (round to +∞)
    return math.ceil(num)
