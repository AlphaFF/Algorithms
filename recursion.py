def total(l):
    if len(l) >= 2:
        return l[0] + total(l[1:])
    else:
        return l[0]


class HashTable:
    def __init__(self):
        self.size = 1
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def bubble_sort(l):
    """冒泡排序."""
    for position in range(len(l) - 1, 0, -1):
        start = 0
        while start < position:
            if l[start] > l[start + 1]:
                l[start], l[start + 1] = l[start + 1], l[start]
            start += 1
    return l


def short_bubble_sort(l):
    """短冒泡排序."""
    exchange = False
    position = len(l) - 1
    while position > 0 and not exchange:
        for i in range(position):
            if l[i] > l[i + 1]:
                exchange = True
                l[i], l[i + 1] = l[i + 1], l[i]
        position -= 1
    return l


def select_sort(l):
    """选择排序, 只交换一次."""
    for p in range(len(l) - 1, 0, -1):
        max_index = 0
        for i in range(p):
            if l[i] <= l[i + 1]:
                max_index = i + 1
        l[p], l[max_index] = l[max_index], l[p]
    return l


def insert_sort(alist):
    """插入排序."""
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current_value


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

    print('Merging', alist)


def merge_sort1(alist):
    """归并排序."""
    if len(alist) > 1:
        mid = len(alist) // 2
        left = merge_sort1([alist[i] for i in range(mid)])
        right = merge_sort1([alist[i] for i in range(mid, len(alist))])
        return merge(left, right)
    return alist


def merge(left, right):
    result = [None] * (len(left) + len(right))
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1

    return result


l0 = [2, 1, 6, 9, 4, 5, 3]
print(bubble_sort(l0))
print(select_sort(l0))

l1 = [1, 2, 4, 20, 11, 12]
print(short_bubble_sort(l1))
print(select_sort(l1))


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
res = merge_sort1(alist)
print(res)


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark += 1

        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

    alist[first], alist[right_mark] = alist[right_mark], alist[first]

    return right_mark


quick_sort(alist)
print(alist)


def quick_sort1(alist, left, right):
    if left >= right:
        return

    low = left
    high = right
    key = alist[low]

    while left < right:
        while left < right and alist[right] > key:
            right -= 1
        while left < right and alist[left] <= key:
            left += 1
        alist[left], alist[right] = alist[right], alist[left]

    alist[right] = key
    quick_sort1(alist, low, left - 1)
    quick_sort1(alist, left + 1, high)


def partition1(alist, left, right):
    x = alist[right]
    i = left - 1
    for j in range(left, right):
        if alist[j] <= x:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[i + 1], alist[right] = alist[right], alist[left]
    return i + 1


def quick_sort2(alist):
    less = []
    equal = []
    greater = []

    if len(alist) > 1:
        pivot = alist[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x ==pivot:
                equal.append(x)
            else:
                greater.append(x)
        return sort(less) + equal + sort(greater)
    else:
        return equal


def quicksort3(alist):
    if len(alist) <= 1:
        return alist
    pivot = alist[0]
    less = [i for i in alist[1:] if i <= pivot]
    greater = [i for i in alist[1:] if i > pivot]
    return quicksort3(less) + [pivot] + quicksort3(greater)


print(quicksort3(alist))
