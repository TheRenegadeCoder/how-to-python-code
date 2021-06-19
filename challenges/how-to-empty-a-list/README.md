## How to Empty a List in Python Challenge

The following challenge was described in the article 
[How to Empty a List in Python](https://therenegadecoder.com/code/how-to-check-if-a-key-exists-in-a-dictionary-in-python/#challenge).

### Challenge Description

Write a function that empties a list only under certain conditions. Since we’re dealing with anime, 
the conditions will be as follows:

- Empty the input list if it meets any of the following conditions:
  - Contains any duplicate shows
  - Contains more than 17 shows
  - Contains shows that feature the word “Your” in the title

### Expected Behavior

```python
to_empty_or_not_to_empty(["Haruhi", "Haruhi"])  # Empty!
to_empty_or_not_to_empty(["Nagatoro"] * 17)  # Empty!
to_empty_or_not_to_empty(["Your Lie in April"])  # Empty!
to_empty_or_not_to_empty(["Steins;Gate", "My Hero Academia", "A Place Further Than the Universe"])  # Do NOT empty!
``` 

### Example Solution

![Solution](solution.jfif)
