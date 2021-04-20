from test_bench import test_bench

def empty_list_by_hand(anime):
    while anime:
        anime.pop()

def empty_list_by_assignment(anime):
    anime = [] # Wouldn't actually work as a function

def empty_list_by_clear(anime):
    anime.clear()

def empty_list_by_del(anime):
    del anime[:]

def empty_list_by_slice_assignment(anime):
    anime[:] = []

def empty_list_by_multiplication(anime):
    anime *= 0  # Also, would not work as a function

test_bench(
    [
        empty_list_by_hand,
        empty_list_by_assignment,
        empty_list_by_clear,
        empty_list_by_del,
        empty_list_by_slice_assignment,
        empty_list_by_multiplication
    ],
    [
        [],
        [1],
        [1, 3, 5],
        [5] * 100
    ]
)
