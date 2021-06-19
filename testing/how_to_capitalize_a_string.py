"""
Tests the performance of all of the solutions listed in the following article:
https://therenegadecoder.com/code/how-to-capitalize-a-string-in-python/
"""


from test_bench import test_bench


def control(_):
    pass


def capitalize_by_hand(string):
    character = string[0]
    if 97 <= ord(character) <= 122:
        shift = ord(character) - 32
        uppercase = chr(shift)
        return uppercase + string[1:]
    return string


def capitalize_by_mapping(string):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character = string[0]
    i = lowercase.find(character)
    return string if i == -1 else uppercase[i] + string[1:]


def capitalize_with_upper(string):
    character = string[0]
    return character.upper() + string[1:]


def capitalize(string):
    return string.capitalize()


test_bench(
    [
        control,
        capitalize_by_hand,
        capitalize_by_mapping,
        capitalize_with_upper,
        capitalize
    ],
    {
        "One Letter String": ["a"],
        "Small String": ["how now brown cow"],
        "Large String": ["One Punch Man" * 100]
    }
)
