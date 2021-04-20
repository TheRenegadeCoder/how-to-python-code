import timeit
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def test_bench(funcs, test_data):
    results = _test_performance(funcs, test_data)
    _show_results(results)

def _test_performance(funcs, test_data):
    num_tests = len(funcs) * len(test_data)
    print(f"> Collecting {num_tests} test(s)")
    results = []
    i = 1
    for test in test_data:
        for func in funcs:
            performance = min(timeit.repeat(lambda: func(test)))
            results.append([func.__name__, test, performance])
            print(f"\t> Test Progress: {i} / {num_tests}")
            i += 1
    print(f"> Testing Complete")
    return pd.DataFrame(results, columns=["Function", "Input", "Performance"])

def _show_results(results):
    print(results.to_string())
    sns.catplot(x="Input", y="Performance", hue="Function", kind="bar", data=pd.DataFrame(results))
    plt.show()
