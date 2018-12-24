def prime_num(n):
    if isinstance(n, str):
        return "Invalid input"
    elif n is None:
        return None
    n = int(n)
    m = n % 2
    p = n % n
    if m is 1 or p is 0:
        return True
    else:
        return False


print(prime_num(5))