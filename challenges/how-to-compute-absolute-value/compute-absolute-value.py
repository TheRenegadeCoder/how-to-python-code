# Link to the challenge: https://therenegadecoder.com/code/how-to-compute-absolute-value-in-python/#challenge
# This solution uses simple math

number = int(input("Enter a number >>> "))
if int((number**2)**0.5) == number: # The number is postive
    print('+' * number)
else: # The number is negative
    print('-' * (-1 * number)) 

