# link to original challenge: https://therenegadecoder.com/code/how-to-check-if-a-key-exists-in-a-dictionary-in-python/#challenge
# Updated challenge: The main challenge was to look for key in the dictionary where all the keys are lowercase. However, in this challange, keys are in randomcase.

dictionary = {
    "fIRe": "combustion or burning, in which substances combine chemically with oxygen from the air and typically give out bright light, heat, and smoke.",

    "Wood": "the hard fibrous material that forms the main substance of the trunk or branches of a tree or shrub, used for fuel or timber.",
    
    "glaSS": "a hard, brittle substance, typically transparent or translucent, made by fusing sand with soda, lime, and sometimes other ingredients and cooling rapidly. It is used to make windows, drinking containers, and other articles."
}

users_key = input("Endter a key here: ")
users_key = users_key.lower()

found = False # Using a boolean variable to check whether the key exist or not

for key in dictionary:
    if key.lower() == users_key:
        found = True
        print(dictionary[key])

if found is not True:
    print("The key doesn't exist in the dictionary")
