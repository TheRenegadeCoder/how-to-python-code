from test_bench import test_bench

def clamp_float_with_branching_nested(num: float, minimum: float, maximum: float):
    if num < minimum:
        return minimum
    elif num > maximum:
        return maximum
    else:
        return num
    
def main() -> None:
    """
    Tests the performance of all the functions defined in this file. 
    """
    test_bench(
        [
            clamp_float_with_branching_nested
        ],
        {
            "Lower Bound": [-.002, 0, .40]
        }
    )


if __name__ == "__main__":
    main()

    
