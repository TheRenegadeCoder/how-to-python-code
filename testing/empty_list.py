from test_bench import test_bench

def control(anime):
    anime = anime.copy()

def empty_list_by_hand(anime):
    anime = anime.copy()
    while anime:
        anime.pop()

def empty_list_by_assignment(anime):
    anime = anime.copy()
    anime = [] # Wouldn't actually work as a function

def empty_list_by_clear(anime):
    anime = anime.copy()
    anime.clear()

def empty_list_by_del(anime):
    anime = anime.copy()
    del anime[:]

def empty_list_by_slice_assignment(anime):
    anime = anime.copy()
    anime[:] = []

def empty_list_by_multiplication(anime):
    anime = anime.copy()
    anime *= 0  # Also, would not work as a function

test_bench(
    [
        control,
        empty_list_by_hand,
        empty_list_by_assignment,
        empty_list_by_clear,
        empty_list_by_del,
        empty_list_by_slice_assignment,
        empty_list_by_multiplication
    ],
    {
        "Empty List": [[]],
        "One Item List": [["Your Lie in April"]],
        "Small List": [["My Hero Academia", "Attack on Titan", "Steins;Gate"]],
        "Large List": [["One Punch Man"] * 100]
    }
)
