def maxSubArray(A):
    if not A:
        return 0

    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(curSum, maxSum)
    return maxSum


if __name__ == '__main__':
    maxSubArray([-2,1,-3,4,-1,2,1,-5,4])