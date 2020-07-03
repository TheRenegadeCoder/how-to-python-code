# Link to the challenge: https://therenegadecoder.com/code/how-to-compute-absolute-value-in-python/#challenge
# This solution using simple string methods

number = input("Enter a number >>> ")
sign = number[0] # It's obviuos that the sign(+ or -) will be at the beginning
value = number[1:]

if sign == '+':
    print('+' * value)
else:
    print('-' * value)
