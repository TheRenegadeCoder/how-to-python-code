"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-create-a-list-in-python/#challenge
"""


def fib_1():
    fibonacci = [1, 1]
    [fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) for i in range(2, 100)]
    return fibonacci


def fib_2():
    series = [1, 1]
    for i in range(2, 100):
        prev_1 = series[i - 1]
        prev_2 = series[i - 2]
        new = prev_1 + prev_2
        series.append(new)
    return series


def fib_3():
    def recur(n):
        if n == 0 or n == 1:
            return 1
        else:
            return recur(n - 1) + recur(n - 2)
    series = []
    for i in range(100):
        number = recur(i)
        series.append(number)
    return series
