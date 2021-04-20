import timeit

def test_bench(funcs, test_data):
    results = {}
    for test in test_data:
        print(f"Current input: {test}")
        for func in funcs:
            performance = min(timeit.repeat(lambda: func(test)))
            print(f"\t{func.__name__}: {performance}")

test_bench([min], [(1, 2, 3)])
