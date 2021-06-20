"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-check-if-a-key-exists-in-a-dictionary-in-python/#challenge
"""


def case_insensitive_lookup(dictionary: dict, term: str):
    """
    Implements a case insensitive lookup using a try/catch

    :author: Muhimen123
    :param dictionary:
    :param term:
    :return:
    """
    key = term.lower()
    try:
        return dictionary[key.lower()]
    except:
        return None
