"""
Tests the performance of all of the solutions listed in the following article:
https://therenegadecoder.com/code/how-to-capitalize-a-string-in-python/
"""

from test_bench import test_bench


def control(_) -> None:
    """
    Provides a control scenario for testing. In this case, none of the functions
    share any overhead, so this function is empty.

    :param _: a placeholder for the string input
    :return: None
    """
    pass


def capitalize_by_hand(string: str) -> str:
    """
    Capitalizes a string by performing a code point shift
    for the first character.

    :param string: an input string
    :return: the capitalized string
    """
    character = string[0]
    if 97 <= ord(character) <= 122:
        shift = ord(character) - 32
        uppercase = chr(shift)
        return uppercase + string[1:]
    return string


def capitalize_by_mapping(string: str) -> str:
    """
    Capitalizes a string by mapping between a set of lowercase
    characters and a set of uppercase characters.

    :param string: an input string
    :return: the capitalized string
    """
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character = string[0]
    i = lowercase.find(character)
    return string if i == -1 else uppercase[i] + string[1:]


def capitalize_with_upper(string: str) -> str:
    """
    Capitalizes a string by leveraging the upper() method of
    strings on the first character.

    :param string: an input string
    :return: the capitalized string
    """
    character = string[0]
    return character.upper() + string[1:]


def capitalize(string: str) -> str:
    """
    Capitalizes a string by leveraging the capitalize() method.
    The behavior of this function differs from he previous
    functions because the capitalize() method also converts all
    other characters int he string to lowercase.

    :param string: an input string
    :return: the capitalized string
    """
    return string.capitalize()


if __name__ == '__main__':
    test_bench(
        {
            "One Letter String": ["a"],
            "Small String": ["how now brown cow"],
            "Large String": ["One Punch Man" * 100]
        }
    )
