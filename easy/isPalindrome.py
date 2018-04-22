#!/usr/bin/env python3
# coding=utf-8


def isPalindrome(x):
    if x < 0:
        return False

    ranger = 1
    while x // ranger >= 10:
        ranger *= 10

    while x:
        left = x // ranger
        right = x % 10
        if left != right:
            return False

        x = (x % ranger) // 10
        ranger //= 100

    return True

def isPalindrome1(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    copy, reverse = x, 0
    while copy:
        reverse *= 10
        reverse += copy % 10
        copy //= 10
    return x == reverse


if __name__ == '__main__':
    # print(isPalindrome(1331))
    print(isPalindrome1(123))