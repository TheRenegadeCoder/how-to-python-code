# link to the challenge: https://therenegadecoder.com/code/how-to-check-if-a-key-exists-in-a-dictionary-in-python/#challenge
# Solution_by: Muhimen123

dictionary = {
    "fire": "combustion or burning, in which substances combine chemically with oxygen from the air and typically give out bright light, heat, and smoke.",

    "wood": "the hard fibrous material that forms the main substance of the trunk or branches of a tree or shrub, used for fuel or timber.",
    
    "glass": "a hard, brittle substance, typically transparent or translucent, made by fusing sand with soda, lime, and sometimes other ingredients and cooling rapidly. It is used to make windows, drinking containers, and other articles."
}

key = input("Enter a key here: ")
key = key.lower()

try:
    print(dictionary[key.lower()])
except:
    print(f"Sorry, the key {key} doesn't exist in the dictionary")
