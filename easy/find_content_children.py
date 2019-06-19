class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        i, j = 0, 0
        count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

    def findContentChildren1(self, g, s):
        g.sort()
        s.sort()
        i, res = 0, 0
        for _ in s:
            if i == len(g):
                break
            if _ >= g[i]:
                res += 1
                i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1, 2], [1, 2, 3]))
