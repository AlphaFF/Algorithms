class Solution:
    import functools

    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs1(self, n: int) -> int:
        fib = nxt = 1
        for _ in range(n):
            fib, nxt = nxt, fib + nxt
        return fib
