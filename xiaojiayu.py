import time


def get_nums(n):
    if not n % 2:
        return (1 + n) * (n // 2)
    else:
        return (n + 1) * (n // 2) + int((n + 1) / 2)


def get_nums1(n):
    numbers = 0
    for i in range(1, n + 1):
        numbers += i
    return numbers


t0 = time.time()
print(get_nums(100000000))
t1 = time.time()
print(t1 - t0)
