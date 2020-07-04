# Link to the challenge: https://therenegadecoder.com/code/how-to-compute-absolute-value-in-python/#challenge
# This solution using simple string methods

number = input("Enter a number >>> ")

if '-' in number: 
    print('-' * (-1 * int(number)))
else:
    print('+' * int(number))
