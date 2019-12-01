class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        tmp = max_ = nums[0]
        n = len(nums)
        for i in range(1, n):
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                max_ = max(max_, tmp, tmp + nums[i], nums[i])
                tmp = nums[i]
        return max_
