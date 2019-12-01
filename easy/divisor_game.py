class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2


if __name__ == '__main__':
    s = Solution()
    print(s.divisorGame(2))
