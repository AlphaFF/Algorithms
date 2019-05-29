class Solution:
    def add_binary(self, a: str, b: str) -> str:
        result = []
        i, j, s = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or s:
            if i >= 0:
                s += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                s += ord(b[j]) - ord('0')
                j -= 1
            result.append(str(s % 2))
            s //= 2
        print(result)
        result.reverse()
        return ''.join(result)

    def add_binary1(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.add_binary1(self.add_binary1(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.add_binary1(a[0:-1], b[0:-1]) + '0'
        else:
            return self.add_binary1(a[0:-1], b[0:-1]) + '1'


if __name__ == '__main__':
    s = Solution()
    print(s.add_binary('1010', '1011'))
    print(s.add_binary1('1010', '1011'))
