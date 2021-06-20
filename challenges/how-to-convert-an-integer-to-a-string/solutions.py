def reverse(num: int) -> str:
    output = ""
    while num != 0:
        output += num % 10
        num //= 10
    return output
