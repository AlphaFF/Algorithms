# -*- coding: utf-8 -*-


def sequential_search(alist, item):
    for i in alist:
        if i == item:
            return True
    return False


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))


def order_sequential_search(alist, item):
    for i in alist:
        if i == item:
            return True
        elif i > item:
            return False
        else:
            continue
    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(order_sequential_search(testlist, 3))
print(order_sequential_search(testlist, 13))


def binary_search(alist, item):
    if len(alist) == 0:
        return False
    start = 0
    end = len(alist) - 1
    mid = (start + end) // 2
    if item < alist[mid]:
        return binary_search(alist[:mid], item)
    elif item == alist[mid]:
        return True
    else:
        return binary_search(alist[mid + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
