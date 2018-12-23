# n_str = input("Enter a number: ")
# n = int(n_str)
# m = 0
# s = 0
# while n != 0:
#     m = n % 10
#     s = (s * 10) + m
#     n = int(n/10)
# print("reverse of the given number is: " + str(s))


def reverse(n):
    if n is None:
        return None
    elif n is "":
        return ""
    elif isinstance(n, str):
        return "invalid input"
    elif n < 0:
        return "invalid input"
    m = 0
    s = 0
    while n != 0:
        m = n % 10
        s = (s * 10) + m
        n = int(n/10)
    return s


print(reverse(21))