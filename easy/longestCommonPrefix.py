#!/usr/bin/env python3
# coding=utf-8


def longestCommonPrefix(strs):
    if not strs:
        return ""

    for index, value in enumerate(zip(*strs)):
        if len(set(value)) > 1:
            return strs[0][:index]
    return min(strs)


if __name__ == '__main__':
    print(longestCommonPrefix(['abc','ab','abcde']))