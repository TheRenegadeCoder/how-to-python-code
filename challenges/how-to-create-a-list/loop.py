# Create a list that contains fibonacci series upto 100
def fib():
    series = [1, 1]
    for i in range(2, 100):
        prev_1 = series[i - 1]
        prev_2 = series[i - 2]
        new = prev_1 + prev_2
        series.append(new)

    return series


fibonacci =  fib()
print(fibonacci)