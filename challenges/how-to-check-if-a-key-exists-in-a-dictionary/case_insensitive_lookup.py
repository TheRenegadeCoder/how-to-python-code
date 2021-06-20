"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-check-if-a-key-exists-in-a-dictionary-in-python/#challenge
"""
from typing import Optional


def case_insensitive_lookup_1(dictionary: dict, term: str) -> Optional[str]:
    """
    Implements a case insensitive lookup using a try/catch.

    :author: Muhimen123
    :param dictionary: a literal dictionary of terms and definitions
    :param term: the term to lookup
    :return: the definition if it exists
    """
    key = term.lower()
    try:
        return dictionary[key.lower()]
    except KeyError:
        return None


def case_insensitive_lookup_2(dictionary: dict, term: str) -> Optional[str]:
    """
    Implements a case insensitive lookup using the get() method.

    :author: jrg94
    :param dictionary: a literal dictionary of terms and definitions
    :param term: the term to lookup
    :return: the definition if it exists
    """
    return dictionary.get(term.lower())
