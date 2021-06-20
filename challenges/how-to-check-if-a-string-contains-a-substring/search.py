"""
Provides a series of solutions to the challenge provided at the following link:
https://therenegadecoder.com/code/how-to-check-if-a-string-contains-a-substring-in-python/#challenge
"""


def search_1(addresses: list, street_number: str, street_name: str) -> list:
    """
    Implements a two-term search functionality using sets.

    :author: jrg94
    :param addresses: a list of addresses
    :param street_number: a street number
    :param street_name: a street name
    :return: a list of street addresses that match the term-term query
    """
    number_matches = set()
    name_matches = set()
    for address in addresses:
        if not street_number or street_number in address: number_matches.add(address)
        if not street_name or street_name in address: name_matches.add(address)
    intersection = number_matches & name_matches
    return list(intersection)
