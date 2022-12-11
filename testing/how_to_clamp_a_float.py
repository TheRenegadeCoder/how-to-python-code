import sys
from inspect import getmembers, isfunction

from test_bench import test_bench


def clamp_float_with_branching_nested(num: float, minimum: float, maximum: float) -> float:
    if num < minimum:
        return minimum
    elif num > maximum:
        return maximum
    else:
        return num


def clamp_float_with_branching_flat(num: float, minimum: float, maximum: float) -> float:
    return minimum if num < minimum else maximum if num > maximum else num


def clamp_float_with_min_and_max(num: float, minimum: float, maximum: float) -> float:
    return max(min(num, maximum), minimum)


def main() -> None:
    """
    Tests the performance of all the functions defined in this file. 
    """
    test_bench(
        [member[1] for member in getmembers(
            sys.modules[__name__], isfunction) if "clamp" in member[0]],
        {
            "Lower Bound": [-.002, 0, .40],
            "Upper Bound": [.402, 0, .40],
            "Between Bounds": [.14, 0, .4]
        }
    )


if __name__ == "__main__":
    main()
