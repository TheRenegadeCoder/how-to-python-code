"""

https://therenegadecoder.com/code/how-to-compute-absolute-value-in-python/#challenge
"""


def absolute_value_text_1(number: int) -> str:
    """
    Creates correct string using arithmetic absolute value.

    :param number: the length and type of the output string
    :return: a string of pluses or minuses based on the input value
    """
    if int((number**2)**0.5) == number:  # The number is positive
        return '+' * number
    else:  # The number is negative
        return '-' * (-1 * number)


def absolute_value_text_2(number: int) -> str:
    """
    Creates correct string using string techniques.

    :param number: the length and type of the output string
    :return: a string of pluses or minuses based on the input value
    """
    if '-' in str(number):
        return '-' * (-1 * int(number))
    else:
        return '+' * int(number)
