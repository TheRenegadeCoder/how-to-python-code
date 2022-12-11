"""
Tests the performance of all of the solutions listed in the following article:
https://therenegadecoder.com/code/how-to-empty-a-list-in-python/
"""

from test_bench import test_bench


def control(anime: list[str]) -> None:
    """
    Provides a control scenario for testing. In this case, all of the solutions
    rely on copying the input list, so the control function accounts for that.

    :param anime: a list of anime 
    """
    anime = anime.copy()


def empty_list_by_hand(anime: list[str]) -> None:
    """
    Empties a list by repeatedly removing elements from a list.  

    :param anime: a list of anime
    """
    anime = anime.copy()
    while anime:
        anime.pop()


def empty_list_by_assignment(anime: list[str]) -> None:
    """
    Empties a list by reassigning the reference.

    :param anime: a list of anime
    """
    anime = anime.copy()
    anime = []  # Wouldn't actually work as a function


def empty_list_by_clear(anime: list[str]) -> None:
    """
    Empties a list by calling the clear method.

    :param anime: a list of anime
    """
    anime = anime.copy()
    anime.clear()


def empty_list_by_del(anime: list[str]) -> None:
    """
    Empties a list by deleting a slice of the list.

    :param anime: a list of anime
    """
    anime = anime.copy()
    del anime[:]


def empty_list_by_slice_assignment(anime: list[str]) -> None:
    """
    Empties a list by replacing a slice of the list with an empty list.

    :param anime: a list of anime
    """
    anime = anime.copy()
    anime[:] = []


def empty_list_by_multiplication(anime: list[str]) -> None:
    """
    Empties a list by multiplication.

    :param anime: a list of anime
    """
    anime = anime.copy()
    anime *= 0  # Also, would not work as a function


if __name__ == "__main__":
    test_bench(
        {
            "Empty List": [[]],
            "One Item List": [["Your Lie in April"]],
            "Small List": [["My Hero Academia", "Attack on Titan", "Steins;Gate"]],
            "Large List": [["One Punch Man"] * 100]
        }
    )
