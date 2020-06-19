# The challenge is to write a script that can generate all the fibonacci numbers form 1 to 100

def using_normal_loops():
    fibonacci = [1, 1]
    for i in range(2, 100):
        previous_number_1 = fibonacci[i - 1]
        previous_number_2 = fibonacci[i - 2]
        new_number = previous_number_1 + previous_number_2
        fibonacci.append(new_number)

    for idx, val in enumerate(fibonacci):
        print(f"{idx+1}: {val}")

def using_recursion(n):
    # Point to be noted: Generating fibonacci numbers with recursion is really slow
    # To speed things up, concepts like memoizition or dynamic programming is applicable
    if n == 0:  return 1
    elif n == 1: return 1
    else: return (using_recursion(n - 1) + using_recursion(n - 2))

using_normal_loops()
for i in range(101):
    print(f"{i+1}: {using_recursion(i)}")

# Using list comprehension
    # This is nothing different than the first one. But in a shorter manner

fibonacci = [1, 1]
[fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) for i in range(2, 100)]
for idx, val in enumerate(fibonacci):
    print(f"{idx + 1}: {val}")
