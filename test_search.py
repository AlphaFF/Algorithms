# reveiw quicksort use python
def test_quickSort1(alist):
    if len(alist) <= 1:
        return alist
    base = alist[0]
    left = []
    right = []
    for _ in alist:
        if _ > base:
            right.append(_)
        else:
            left.append(_)
    return test_quickSort(left) + [base] + test_quickSort(right)

def partition(alist, first, last):
    reference_value = alist[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and alist[left] <= reference_value:
            left += 1
        while right >= left and alist[right] >= reference_value:
            right -= 1
        if right < left:
            done = True
        else:
        # change the values
            alist[left], alist[right] = alist[right], alist[left]
    alist[first], alist[right] = alist[right], alist[first]
    return right


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


alist = [54,26,93,17,77,31,44,55,20] 
quickSort(alist)
print(alist)





