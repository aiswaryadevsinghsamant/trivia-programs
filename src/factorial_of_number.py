def factorial_num(n):
    if isinstance(n, str):
        return "Invalid input"
    elif n is None:
        return None
    n = int(n)
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    return fact


# print(factorial_num(5))
# print(factorial_num(input("Enter a number: ")))