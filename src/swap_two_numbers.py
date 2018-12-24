def swap_using_thirdvariable(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return "Invalid input"
    elif a or b is None:
        return None
    a = int(a)
    b = int(b)
    c = a
    a = b
    b = c
    return a, b


# print(swap_using_thirdvariable(5, 4))
# print(swap_using_thirdvariable(input("Enter a number: "), input("Enter another number: ")))
# print(str(swap_using_thirdvariable(5, 4)) + " are the reversed numbers")


def swap_without_thirdvariable(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return "Invalid input"
    elif a or b is None:
        return None

    a = int(a)
    b = int(b)
    a = a + b
    b = a - b
    a = a - b
    return a, b


# print(swap_without_thirdvariable(5, 7))
# print(str(swap_without_thirdvariable(5, 7)) + "are the reversed numbers")
# print(swap_without_thirdvariable(input("Enter a number:"), input("Enter another number:")))
