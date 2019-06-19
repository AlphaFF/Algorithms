class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        result = int(''.join([str(_) for _ in A])) + K
        return [int(_) for _ in str(result)]

    # def addToArrayForm1(self, A, K):
    #     for i in range(len(A))[::-1]:
    #         A[i], K = (A[i] + K) % 10, (A[i] + K) / 10
    #     return [int(i) for i in str(K)] + A if K else A

    def addToArrayForm2(self, A, K):
        i = 0
        j = 0
        for a in A:
            i = i + (a * (10**(len(A) - 1 - j)))
            j += 1
        return [int(x) for x in str(i + K)]


if __name__ == '__main__':
    s = Solution()
    print(s.addToArrayForm2([2, 1, 5], 806))
