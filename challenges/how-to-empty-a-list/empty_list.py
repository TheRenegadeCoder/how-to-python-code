def to_empty_or_not_to_empty(anime: list):
    hasDuplicates = len(set(anime)) != len(anime)
    hasSeventeenShows = len(anime) == 17
    hasYourTitle = any("Your" in word for word in anime)
    if hasDuplicates or hasSeventeenShows or hasYourTitle:
        anime.clear()
