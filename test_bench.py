import timeit

def test_bench(funcs, test_data):
    num_tests = len(funcs) * len(test_data)
    print(f"> Collecting {num_tests} test(s)")
    results = {}
    i = 1
    for test in test_data:
        results[test] = {}
        for func in funcs:
            performance = min(timeit.repeat(lambda: func(test)))
            results[test][func.__name__] = performance
            print(f"\t> Test Progress: {i} / {num_tests}")
            i += 1
    print(f"> Testing Complete")
    return results

def show_results(results):
    print("> Displaying Results")
    for test in results:
        print(f"\t> Input: {test}")
        for func in results[test]:
            print(f"\t\t> {func}: {results[test][func]}")
    print("> Results Displayed")

results = test_bench([min, max], [(1, 2, 3), (-1, 4, 13)])
show_results(results)
