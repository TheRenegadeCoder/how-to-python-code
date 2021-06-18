def search(addresses: list, street_number: str, street_name: str) -> list:
    number_matches = set()
    name_matches = set()
    for address in addresses:
        if not street_number or street_number in address: number_matches.add(address)
        if not street_name or street_name in address: name_matches.add(address)
    intersection = number_matches & name_matches
    return list(intersection)
