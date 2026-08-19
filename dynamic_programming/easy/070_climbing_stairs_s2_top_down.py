class Solution:
    def computeClimbStairs(self, n: int, cache: dict) -> int:
        if n == 1 or n == 2:
            cache[n] = n
            return cache[n]

        cache[n] = (cache[n - 1] if (n - 1) in cache else self.computeClimbStairs(n - 1, cache)) + (cache[n - 2] if (n - 2) in cache else self.computeClimbStairs(n - 2, cache))
        return cache[n]

    def climbStairs(self, n: int) -> int:
        cache = {}

        return self.computeClimbStairs(n, cache)