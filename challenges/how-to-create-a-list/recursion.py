# Create a list that contains all the number upto 100
# NOTE: Using recursion can be really slow. To speed things up, concepts like memoizition and dynamic programming in applicable
def recur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (recur(n - 1) + recur(n - 2))

series = []
for i in range(100):
    number = recur(i)
    series.append(number)

print(series)