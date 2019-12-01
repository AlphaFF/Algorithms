class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 前一家的收益或者前前家的收益加上当前家的利益
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        p = nums[0]
        q = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            p, q = q, max(p + nums[i], q)

        return q

    def rob1(self, nums):
        # 偷不偷
        rob = no_rob = 0
        for n in nums:
            no_rob, rob = max(no_rob, rob), no_rob + n
        return max(rob, no_rob)
