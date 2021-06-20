"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-iterate-over-multiple-lists-at-the-same-time-in-python/#challenge
"""


def next_pokemon_1(pokemon, levels, fainted):
    best_level = -1
    best_choice = pokemon[0]
    for curr_pokemon, level, has_fainted in zip(pokemon, levels, fainted):
        if not has_fainted and level > best_level:
            best_level = level
            best_choice = curr_pokemon
    return best_choice
