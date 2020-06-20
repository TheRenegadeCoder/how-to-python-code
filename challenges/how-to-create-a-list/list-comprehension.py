fibonacci = [1, 1]
[fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) for i in range(2, 100)]

print(fibonacci)