def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    start = 0
    found = False
    while start < len(nums) - 1 and not found:
        for i in range(start + 1, len(nums)):
            if nums[start] + nums[i] == target:
                found = True
                return [start, i]
        start += 1
    return [-1, -1]


def two_sum(nums, target):
    d = {}
    for i, v in enumerate(nums):
        if v not in d:
            d[target - v] = i
        else:
            return d[v], i
    return [-1, -1]


print(two_sum([2, 7, 11, 13], 13))


def reverse(x):
    if x > 0:
        y = int(str(x)[::-1])
        return y if y < 2 ** 31 - 1 else 0
    else:
        y = -int(str(x)[::-1].rstrip('-'))
        return y if y > -2 ** 31 else 0


def reverse1(x):
    sign = 1 if x > 0 else - 1
    tmp = abs(x)

    reverse = 0

    while tmp > 0:
        reverse += tmp % 10
        tmp = tmp // 10
        if not tmp:
            break
        reverse *= 10
    if reverse < (-2) ** 31 or reverse > 2 ** 31 - 1:
        return 0
    return reverse * sign


print(reverse1(-1534))
