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


def clamp_float_with_sorting(num: float, minimum: float, maximum: float) -> float:
    sorted([num, minimum, maximum])[1]

if __name__ == "__main__":
    test_bench(
        {
            "Lower Bound": [-.002, 0, .40],
            "Upper Bound": [.402, 0, .40],
            "Between Bounds": [.14, 0, .4]
        }
    )
