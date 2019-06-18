class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = [int(_) for _ in str(num)]
        new_num = sum(l)
        if sum(l) < 10:
            return new_num
        else:
            return self.addDigits(new_num)

    def addDigits1(self, num):
        if not num:
            return num
        if num % 9 == 0:
            return 9
        else:
            return num % 9

    def addDigits2(self, num):
        return num if not num else num % 9 or 9


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits2(1384))
