"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-capitalize-a-string-in-python/#challenge
"""


def capitalize_1(string):
    return string[0].upper() + string[1:].lower()
