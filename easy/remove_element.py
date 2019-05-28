class Solution:
    def remove_element(self, nums, val):
        for i, v in enumerate(nums):
            if v == val:
                del nums[i]
        print(nums)
        return len(nums)

    def remove_element1(self, nums, val):
        """有问题"""
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            else:
                j += 1
        print(nums)
        return len(nums)

    def remove_element2(self, nums: list, val: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        print(nums[:start])
        return start


if __name__ == '__main__':
    s = Solution()
    print(s.remove_element2([3, 2, 2, 3], 3))
