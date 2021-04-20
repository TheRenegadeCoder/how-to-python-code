import timeit
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import copy

def test_bench(funcs: list, test_data: dict):
    results = _test_performance(funcs, test_data)
    _show_results(results)

def _test_performance(funcs: list, test_data: dict) -> pd.DataFrame:
    num_tests = len(funcs) * len(test_data)
    print(f"> Collecting {num_tests} test(s)")
    results = []
    i = 0
    for name, test in test_data.items():
        for func in funcs:
            print(f"\t> Test Progress: {i + 1} / {num_tests}")
            print(f"\t\t> Function Name: {func.__name__}")
            print(f"\t\t> Test Name: {name}")
            performance = min(timeit.repeat(lambda: func(*test)))
            results.append([func.__name__, name, performance])
            i += 1
    print(f"> Testing Complete")
    return pd.DataFrame(results, columns=["Function", "Input", "Performance"])

def _show_results(results: pd.DataFrame):
    print(results.to_string()) 
    sns.set_theme()
    with sns.plotting_context("paper", font_scale=1.5):
        sns.catplot(x="Input", y="Performance", hue="Function", kind="bar", data=pd.DataFrame(results), legend=False, height=8, aspect=2)
    plt.title("How to Python: Function Performance Comparison", fontsize=16)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, title="Functions", fontsize='12', title_fontsize='12')
    plt.tight_layout()
    plt.show()
