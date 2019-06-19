class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return n
        i = 1
        while 1:
            n -= i
            if n > i:
                i += 1
            else:
                break
        return i

    def arrangeCoins1(self, n):
        k = 1
        while n >= 0:
            n -= k
            k += 1
        return k - 2


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins1(8))
