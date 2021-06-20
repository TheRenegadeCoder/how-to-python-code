"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-increment-a-number-in-python/#challenge
"""


def inc(num: int):
    ans = num
    if num % 2 == 0:
        ans += 3
    else:
        ans += 1

    if num % 5 == 0:
        ans += 5
    return ans
