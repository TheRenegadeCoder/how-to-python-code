"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-capitalize-a-string-in-python/#challenge
"""


def capitalize_1(string):
    """
    Capitalizes a string using a combination of the upper and lower methods.

    :author: jrg94
    :param string: any string
    :return: a string with the first character capitalized and the rest lowercased
    """
    return string[0].upper() + string[1:].lower()
