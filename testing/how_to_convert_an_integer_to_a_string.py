"""
Tests the performance of all of the solutions listed in the following article:
https://therenegadecoder.com/code/how-to-convert-an-integer-to-a-string-in-python/#performance
"""

from test_bench import test_bench


def control(_):
    """
    Provides a control scenario for testing. In this case, none of the functions
    share any overhead, so this function is empty.

    :param _: a placeholder for the int input
    :return: None
    """
    pass


def convert_by_type_casting(integer: int) -> str:
    """
    Converts an integer to a string by type casting.

    :param integer: an integer
    :return: the integer as a string
    """
    return str(integer)


def convert_by_f_string(integer: int) -> str:
    """
    Converts an integer to a string using f-strings.

    :param integer: an integer
    :return: the integer as a string
    """
    return f"{integer}"


def convert_by_interpolation(integer: int) -> str:
    """
    Converts an integer to a string using string interpolation.

    :param integer: an integer
    :return: the integer as a string
    """
    return "%s" % integer


def main() -> None:
    """
    Tests the performance of all the functions defined in this file.
    """
    test_bench(
        [
            control,
            convert_by_type_casting,
            convert_by_f_string,
            convert_by_interpolation
        ],
        {
            "Zero": [0],
            "Single Digit": [5],
            "Small Number": [1107321],
            "Massive Number": [2 ** 64]
        }
    )


if __name__ == '__main__':
    main()
