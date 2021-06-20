"""
Tests the performance of all of the solutions listed in the following article:
https://therenegadecoder.com/code/how-to-convert-an-integer-to-a-string-in-python/#performance
"""

from test_bench import test_bench


def control(_):
    pass


def convert_by_type_casting(integer: int) -> str:
    return str(integer)


def convert_by_f_string(integer: int) -> str:
    return f"{integer}"


def convert_by_interpolation(integer: int) -> str:
    return "%s" % integer


def main():
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
