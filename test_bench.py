import timeit

def test_bench(funcs, test_data):
    for func in funcs:
        for test in test_data:
            print(min(timeit.repeat(lambda: func(test))))

test_bench([min], [(1, 2, 3)])
