#!/usr/bin/env python3
# coding=utf-8

def is_valid(s):
    stack, lookup = [], {')': '(', ']': '[', '}': '{'}
    for parenthese in s:
        if parenthese in lookup.values():
            stack.append(parenthese)
        elif parenthese in lookup.keys():
            if len(stack) == 0 or lookup[parenthese] != stack.pop():
                return False
        else:
        	return False
    return len(stack) == 0


if __name__ == '__main__':
    is_valid('()')