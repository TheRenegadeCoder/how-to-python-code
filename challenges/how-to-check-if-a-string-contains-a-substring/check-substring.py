addresses = [
        "123 Elm Street",
        "123 Oak Street",
        "678 Elm Street"
        ]

user_address = input("Enter an address: ")
for address in addresses:
    if user_address.lower() in address.lower(): # Making the search case incencitive
        print(address)

