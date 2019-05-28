class Solution:
    def str_str(self, haystack: str, needle: str):
        return haystack.find(needle)

    def str_str1(self, haystack: str, needle: str):
        p, q = len(haystack), len(needle)
        for i in range(p - q + 1):
            if haystack[i: i + q] == needle:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.str_str1('hello', 'll'))
