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


# 冒泡排序
def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(alist)
print(alist)


# 短冒泡排序
def short_bubble_sort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1


# 选择排序, 只交换一次
def selection_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        pos_max = 0
        for j in range(1, i + 1):
            if alist[j] > alist[pos_max]:
                pos_max = j
        alist[i], alist[pos_max] = alist[pos_max], alist[i]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(alist)
print(alist)


# 插入排序
def insert_sort(alist):
    for index in range(1, len(alist)):
        cur = alist[index]
        pos = index
        while pos > 0 and alist[pos - 1] > cur:
            alist[pos] = alist[pos - 1]
        alist[pos] = cur
