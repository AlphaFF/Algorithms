class Solution:
    def add_strings(self, nums1: str, nums2: str) -> str:
        result = []
        i, j, carry = len(nums1) - 1, len(nums2) - 1, 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(nums1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(nums2[j]) - ord('0')
                j -= 1
            result.append(str(carry % 10))
            carry //= 10
        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.add_strings('125', '2347'))
