import timeit
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def test_bench(funcs: list, test_data: list):
    def control(*args): pass
    funcs.insert(0, control)
    results = _test_performance(funcs, test_data)
    _show_results(results)

def _test_performance(funcs: list, test_data: list) -> pd.DataFrame:
    num_tests = len(funcs) * len(test_data)
    print(f"> Collecting {num_tests} test(s)")
    results = []
    i = 0
    for test in test_data:
        for func in funcs:
            print(f"\t> Test Progress: {i + 1} / {num_tests}")
            print(f"\t\t> Function Name: {func.__name__}")
            performance = min(timeit.repeat(lambda: func(test.copy())))
            results.append([func.__name__, f"Test #{i // len(funcs) + 1}", performance])
            i += 1
    print(f"> Testing Complete")
    return pd.DataFrame(results, columns=["Function", "Input", "Performance"])

def _show_results(results: pd.DataFrame):
    print(results.to_string()) 
    sns.set_theme()
    sns.set_context("paper")
    sns.catplot(x="Input", y="Performance", hue="Function", kind="bar", data=pd.DataFrame(results), legend=False, height=8, aspect=2)
    plt.title("How to Python: Function Performance Comparison", fontsize=16)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title="Functions", fontsize='12', title_fontsize='12')
    plt.tight_layout()
    plt.show()
