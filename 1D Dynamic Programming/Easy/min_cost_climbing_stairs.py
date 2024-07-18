class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)     
        minCost = [0 for i in range(n + 1)]

        idx = n - 1
        while idx >= 0:
            if idx == n - 1:
                minCost[idx] = cost[idx] + minCost[idx + 1]
            else:
                minCost[idx] =cost[idx] + min(minCost[idx + 1], minCost[idx + 2])
            idx -= 1

        return min(minCost[0], minCost[1])
