"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-remove-duplicates-from-a-list-in-python/#challenge
"""


def remove_dupes_1(dupes: list):
    def is_dupe(item, counts):
        if item not in counts:
            counts[item] = 1
            return False
        else:
            return True

    counts = dict()
    dupes[:] = [item for item in dupes if not is_dupe(item, counts)]
