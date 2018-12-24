
def amstrong_num(n):
    if isinstance(n, str):
        return "Invalid input"
    elif n is None:
        return  None
    n = int(n)
    t = n
    s = 0
    m = 0
    while n != 0:
        m = n % 10
        s = s + (m * m * m)
        n = int(n/10)
    if t == s:
        return True
    else:
        return False
# print(amstrong_num(153))