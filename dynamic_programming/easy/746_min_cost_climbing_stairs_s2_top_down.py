class Solution:
    def computeMinCostClimbingStairs(self, cost: List[int], n: int, cache: dict) -> int:
        if n == 0 or n == 1:
            cache[n] = cost[n]
            return cache[n]
        
        if (n - 1) not in cache:
            cache[n - 1] = self.computeMinCostClimbingStairs(cost, n - 1, cache)
        if (n - 2) not in cache:
            cache[n - 2] = self.computeMinCostClimbingStairs(cost, n - 2, cache)

        prev1 = cache[n - 1] + cost[n - 1] if (n - 1) > 1 else cache[n - 1]
        prev2 = cache[n - 2] + cost[n - 2] if (n - 2) > 1 else cache[n - 2]
        cache[n] = min(prev1, prev2)

        return cache[n]


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        return self.computeMinCostClimbingStairs(cost, n, cache)