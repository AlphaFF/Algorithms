def is_valid(s):
    if not s:
        return True
    d = {'}': '{', ']': '[', ')': '('}
    stack = []
    for i in s:
        if i in '{[(':
            stack.append(i)
        else:
            if not stack or stack.pop() != d[i]:
                return False
    return False if stack else True


s = '['
print(is_valid(s))
