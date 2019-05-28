def remove_duplicates(nums):
    k = 1
    for _ in nums:
        if _ != nums[k - 1]:
            nums[k] = _
            k += 1
    return k


def remove_duplicates1(nums: list) -> int:
    if not nums:
        return 0
    i, j = 1, 1
    while j < len(nums):
        if nums[i - 1] != nums[j]:
            nums[i] = nums[j]
            i += 1
        j += 1
    print(i, nums)
    return i


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates1([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
