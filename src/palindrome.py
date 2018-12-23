# n_str = input("Enter a number: ")
# n = int(n_str)
# t = n
# m = 0
# s = 0
# while n != 0:
#     m = n % 10
#     s = (s * 10) + m
#     n = int(n/10)
# if s == t:
#     print(str(t) + "is a palindrome")
# else:
#     print(str(t) + "is not a palindrome")





# from reverse_of_numbers import reverse
#
#
# def palindrome(n):
#     n = int(n)
#     t = n
#     s = reverse(n)
#     if t == s:
#         return True
#     else:
#         return False
#
#
# print(palindrome(input("Enter a number: ")))


def palindrome_fun(n):
    if isinstance(n, str):
        return "invalid input"
    n = int(n)
    t = n
    m = 0
    s = 0
    while n != 0:
        m = n % 10
        s = (s * 10) + m
        n = int(n/10)
    if t == s:
        return True
    else:
        return False


# print(palindrome_fun(input("Enter a number: ")))





