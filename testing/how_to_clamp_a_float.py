"""
Tests the performance of all of the solutions listed in the following article:
https://therenegadecoder.com/code/how-to-clamp-a-floating-point-number-in-python/
"""

from test_bench import test_bench


def control(*_) -> None:
    """
    Provides a control scenario for testing. In this case, none of the functions
    share any overhead, so this function is empty.

    :param _: a placeholder for the string input
    :return: None
    """
    pass


def clamp_float_with_branching_nested(num: float, minimum: float, maximum: float) -> float:
    """
    Clamps a float between two bounds using a series of if statements.

    :param num: the value to clamp
    :param minimum: the lower bound
    :param maximum: the upper bound
    :return: a value in the range of minimum and maximum
    """
    if num < minimum:
        return minimum
    elif num > maximum:
        return maximum
    else:
        return num


def clamp_float_with_branching_flat(num: float, minimum: float, maximum: float) -> float:
    """
    Clamps a float between two bounds using a series of ternary statements.

    :param num: the value to clamp
    :param minimum: the lower bound
    :param maximum: the upper bound
    :return: a value in the range of minimum and maximum
    """
    return minimum if num < minimum else maximum if num > maximum else num


def clamp_float_with_min_and_max(num: float, minimum: float, maximum: float) -> float:
    """
    Clamps a float between two bounds using a mix of min and max functions.

    :param num: the value to clamp
    :param minimum: the lower bound
    :param maximum: the upper bound
    :return: a value in the range of minimum and maximum
    """
    return max(min(num, maximum), minimum)


def clamp_float_with_sorting(num: float, minimum: float, maximum: float) -> float:
    """
    Clamps a float between two bounds using a sorting technique.

    :param num: the value to clamp
    :param minimum: the lower bound
    :param maximum: the upper bound
    :return: a value in the range of minimum and maximum
    """
    sorted([num, minimum, maximum])[1]


if __name__ == "__main__":
    test_bench(
        {
            "Lower Bound": [-.002, 0, .40],
            "Upper Bound": [.402, 0, .40],
            "Between Bounds": [.14, 0, .4],
            "Large Numbers": [123456789, -432512317, 5487131463]
        }
    )
