"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-check-if-a-key-exists-in-a-dictionary-in-python/#challenge
"""


def to_empty_or_not_to_empty_1(anime: list):
    has_duplicates = len(set(anime)) != len(anime)
    has_seventeen_shows = len(anime) == 17
    has_your_title = any("Your" in word for word in anime)
    if has_duplicates or has_seventeen_shows or has_your_title:
        anime.clear()
