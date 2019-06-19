class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_nums = sorted(nums)
        return sum([tmp_nums[i] for i in range(len(tmp_nums)) if not i % 2])

    def arrayPairSum1(self, nums):
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum1([1, 4, 3, 2]))
