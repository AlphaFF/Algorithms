class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits:
            return False
        if len(bits) == 1:
            if bits[0] == 0:
                return True
            else:
                return False
        else:
            if bits[0] == 0:
                return self.isOneBitCharacter(bits[1:])
            else:
                return self.isOneBitCharacter(bits[2:])

    def isOneBitCharacter1(self, bits):
        if not bits:
            return False
        n = len(bits)
        index = 0
        while index < n:
            if index == n - 1:
                return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isOneBitCharacter([1, 0, 0]))
