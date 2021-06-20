"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-convert-an-integer-to-a-string-in-python/#challenge
"""


def reverse_1(num: int) -> str:
    output = ""
    while num != 0:
        output += num % 10
        num //= 10
    return output
