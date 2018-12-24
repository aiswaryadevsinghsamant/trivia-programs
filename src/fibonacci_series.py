def fibonacci_ser(n):
    if isinstance(n, str):
        return "Invalid input"
    elif n is None:
        return None
    n = int(n)
    temp = list()     # temp is an empty list (i.e temp = [])
    temp.append(0)
    temp.append(1)
    i = 2             # i is the index of list temp
    # while i < n:
    while len(temp) < n:       # loop will continue until length of list(i.e temp) is < length of fibonacci series
        x = temp[i-2] + temp[i-1]
        temp.append(x)
        i += 1
    return temp


# print(fibonacci_ser(9))
# print(fibonacci_ser(input("Enter the series  ")))



def fibonacci_fixed_ser(n):
    n = int(n)
    temp = [None]*9
    temp[0] = 0
    temp[1] = 1
    i = 2
    while i < n:
        temp[i] = temp[i-2] + temp[i-1]
        i = i + 1

    return temp


print(fibonacci_fixed_ser(9))

