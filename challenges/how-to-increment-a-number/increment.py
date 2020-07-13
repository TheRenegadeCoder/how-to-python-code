num = int(input("Enter a number: "))
ans = num
if num % 2 == 0:
    ans += 3
else:
    ans += 1

if num % 5 == 0:
    ans += 5

print(ans)


