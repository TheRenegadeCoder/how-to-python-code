"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-remove-duplicates-from-a-list-in-python/#challenge
"""


def remove_dupes():
    def is_dupe(item, counts):
        if item not in counts:
            counts[item] = 1
            return False
        else:
            return True

    dupes = [1, 3, 8, 3, 5]
    counts = dict()
    dupes[:] = [item for item in dupes if not is_dupe(item, counts)]
