#!/usr/bin/env python3
# coding:utf-8

# # two sum
# # 给定一个整数数组，找出其中两个数满足相加等于你指定的目标数字。
# # 要求：这个函数twoSum必须要返回能够相加等于目标数字的两个数的索引
#
# # 思路很特别,需要复习
# def twoSum(nums, target):
#     if len(nums) <= 1:
#         return False
#     d = {}
#     for i in range(len(nums)):
#         if nums[i] in d:
#             return [d[num[i]], i]
#         else:
#             d[target - num[i]] = i
#
#
# # reverse integer
# def test_reverseInteger(s):
#     '''
#     1.把整数转为字符串
#     2.取第一位如果有-号先把-号放在一边
#     3.从最后一位开始取,如果是0,并且新的字符串为空时,去掉0
#     '''
#     s = list(str(s))
#     sign = '-' if s[0] == '-' else ''
#     new = []
#     for i in range(len(s) - 1, -1, -1):
#         print(i)
#         if (not new and s[i] == '0') or s[i] == '-':
#             pass
#         else:
#             new.append(s[i])
#     r = [sign] + new
#     print(r)
#     return int(r)
#
#
# def test_reverseInteger1(s):
#     '''
#     1.把数字转为10**n
#     2.把n存到一个地方
#     '''
#     pass
#
#
# def reverse(x):
#     s = (x > 0) - (x < 0)
#     r = int(str(s * x)[::-1])
#     return s * r * (r < 2 ** 31)
#
#
# # test_reverseInteger(-123)
# # s = reverse(123)
# # print(s)
#
# # palindrome number
# # 判断一个数字是不是回文数字
# # 这个有问题,题目要求是不使用额外空间,
# def test_palindromeNumber(x):
#     '''
#     1.把数字转为字符串
#     2.判断字符串是不是回文字符串即可
#     3.复数肯定不是回文字符串
#     '''
#     x = str(abs(x))
#     palindrome = True
#     l = 0
#     r = len(x) - 1
#     while l < r and palindrome:
#         if x[l] == x[r]:
#             l += 1
#             r -= 1
#         else:
#             palindrome = False
#     return palindrome
#     pass
#
#
# # 没看懂...
# def isPalindrome(x):
#     if x < 0: return False
#     r = 1
#     while x / r >= 10:
#         r += 10
#     while x:
#         left = x / r
#         right = x % 10
#         if left != right:
#             return False
#         x = (x % r) / 10
#         r /= 100
#     return True
#
#
# # longest common prefix
# # 求所有字符串的最长公共前缀，即数组的所有字符串都包含这个前缀
# def test_longestCommonPrefix(strs):
#     s = sorted(strs, key=len)
#     pass
#
#
# # 使用zip和set
# def longestCommonPrefix(strs):
#     if not strs:
#         return ''
#     for i, letter_group in enumerate(zip(*strs)):
#         if len(set(letter_group)) > 1:
#             return strs[0][:i]
#     else:
#         return min(strs, key=len)
#
#
# # valid parentheses
# # 有效的括号
# def test_validParentheses(s):
#     s = {')': '(', '}': '{', ']': '['}
#     stack = ['1']
#     valid = True
#     pos = 0
#     while pos < len(s) and valid:
#         if s[pos] in s.keys():
#             if s[pos] != stack.pop():
#                 valid = False
#         if s[pos] in s.values():
#             stack.append(s[pos])
#         pos += 1
#     return valid
#
#
# def validParentheses(s):
#     stack = []
#     d = {')': '(', '}': '{', ']': '['}
#     for char in s:
#         if char in d.values():
#             stack.append(char)
#         elif char in d.keys():
#             if stack == [] or d[char] != stack.pop():
#                 return False
#         else:
#             return False
#     return not stack
#
#
# # merge two sorted lists
# def test_mergeTwoLists(l1, l2):
#     i = 0
#     j = 0
#     s = []
#     while i < len(l1) and j < len(l2):
#         while l1[i] <= l2[j] and i < len(l1):
#             s.append(l1[i])
#             i += 1
#         while l1[i] > l2[j] and j < len(l2):
#             s.append(l2[j])
#             j += 1
#     return s

# # 没看懂
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return '{} -> {}'.format(self.val, self.next)


#
#
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListCode
#         :type l2: ListCode
#         """
#         curr = dummy = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next
#         curr.next = l1 or l2
#         return dummy.next
#
#
# if __name__ == '__main__':
#     l1 = ListNode(0)
#     print(l1)
#     l1.next = ListNode(1)
#     print((l1))
#     l2 = ListNode(2)
#     l2.next = ListNode(3)
#     print(Solution().mergeTwoLists(l1, l2))

# Reverse Linked List
# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype ListNode
#         """
#         prev = None
#         while head:
#             curr = head
#             head = head.next
#             curr.next = prev
#             prev = curr
#         return prev


# class Solution:
#     def removeDuplicates(self,nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         practice // error
#         """
#         l = []
#         for i in range(len(nums)):
#             if nums[i] not in l:
#                 l.append(nums[i])
#         return len(l)

#     def removeDuplicates1(self,nums):
#         """
#         copy
#         只需维持一个新的索引值来重新复制列表即可
#         """
        # if not nums:
        #     return 0
        # newTail = 0
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[newTail]:
        #         newTail += 1
        #         nums[newTail] = nums[i]
        # return newTail + 1

# class Solution:
#     def removeElement(self,nums,val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         test
#         """
#         i, total = 0, len(nums)
#         while i < total:
#             if nums[i] == val:
#                 nums.pop(i)
#                 total -= 1
#             else:
#                 i += 1
#         return len(nums)

#     def removeElement1(self,nums,val):
#         """
#         copy
#         只需要长度,不需要列表,每次判断值时,如果相等,把这个值丢到最后
#         """
#         start, end = 0, len(nums) - 1
#         while start <= end:
#             if nums[start] == val:
#                 nums[start], nums[end], end = nums[end], nums[start], end - 1
#             else:
#                 start += 1
#         return start


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        test
        """
        return haystack.find(needle)
    
    def strStr(self, haystack, needle):
        """
        copy
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        test
        """
        start = 0
        while start < len(nums):
            if nums[start] == target:
                return start
            elif nums[start] > target:
                nums.insert(start,target)
                return start
            elif nums[start] < target:
                start += 1
        return start

    def searchInsert(self, nums, target):
        """
        copy
        由于列表已经排序过,所以只要找出比target小的即可
        """
        return len([x for x in nums if x < target])


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

    def countAndSay(self, n):
        """
        没看懂
        :param n:
        :return:
        """
        import re
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

# 求最大子数组之和
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        copy
        """
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num,curSum+num)
            maxSum = max(maxSum,curSum)
        return maxSum

# 求最后一个字符串的长度
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        注意' '的干扰
        """
        return len(s.rstrip(' ').split(' ')[-1])


# 给你一个用数组表示的数，求加一之后的结果，结果还是用数组表示
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         test
#         """
#         s = ''.join(str(i) for i in digits)
#         s = str(int(s) + 1)
#         return [int(x) for x in s]

#     def plusOne(self, digits):
#         """
#         copy
#         """
#         num = 0
#         for i in range(len(digits)):
#             num += digits[i] * pow(10,len(digits)-1-i)
#         return [int(i) for i in str(num+1)]


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0:return b
        if len(b)==0:return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1],b[0:-1]) + '1'

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1 



    
