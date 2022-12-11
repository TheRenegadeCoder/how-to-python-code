import inspect
import os
import timeit
from inspect import getmembers, isfunction

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def test_bench(test_data: dict):
    """
    Given a list of functions and a list of dictionary of test data,
    this function will execute performance testing using all of the items
    in the dictionary on all of the functions provided.

    Dictionary must be in the form of the following:

    {"test_1_name": ["list", "of", "arguments"]}

    :param funcs: a list of functions
    :param test_data: a dictionary of test data
    """
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    funcs = [
        member[1] for member in getmembers(module, isfunction)
        if not "test_bench" in member[0]
    ]
    results = _test_performance(funcs, test_data)
    _show_results(results)


def _test_performance(funcs: list, test_data: dict) -> pd.DataFrame:
    """
    Given a list of functions and a dictionary of test data, this function
    creates a DataFrame containing the name of the function, the input to
    that function, and the resulting performance of that combination. A row
    is generated for all possible combinations of functions and test data items.

    :param funcs: a list of functions
    :param test_data: a dictionary of test data
    """
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
    """
    Given a DataFrame of performance testing results, this function
    plots the results in a figure. In addition, it dumps the results as a string.

    :param results: a DataFrame containing the results of a performance test
    """
    print(results.to_string())
    sns.set_theme()
    with sns.plotting_context("paper", font_scale=1.5):
        sns.catplot(
            x="Input",
            y="Performance",
            hue="Function",
            kind="bar",
            data=pd.DataFrame(results),
            legend=False,
            height=8,
            aspect=2
        )
    plt.title("How to Python: Function Performance Comparison", fontsize=16)
    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc=2,
        title="Functions",
        fontsize='12',
        title_fontsize='12'
    )
    plt.tight_layout()
    filename = os.path.splitext(
        os.path.basename(inspect.stack()[2].filename)
    )[0]
    plt.savefig(f"{os.path.join('testing', 'visualizations', filename)}.png")
