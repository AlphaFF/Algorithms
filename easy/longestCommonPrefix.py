#!/usr/bin/env python3
# coding=utf-8


def longestCommonPrefix(strs):
    if not strs:
        return ""

    for index, value in enumerate(zip(*strs)):
        if len(set(value)) > 1:
            return strs[0][:index]
    return min(strs)


def longest_common_prefix(strs):
    if not strs:
        return ''
    length = len(min(strs, key=len))
    print(length)
    s = ''
    index = 0
    while index < length:
        u = set()
        for word in strs:
            if word[index] not in u:
                u.add(word[index])
            if len(u) > 1:
                return s
        s += u.pop()
        index += 1

    return s


print(longest_common_prefix(['abc', 'ab', 'abcde']))


# if __name__ == '__main__':
#     print(longestCommonPrefix(['abc', 'ab', 'abcde']))
