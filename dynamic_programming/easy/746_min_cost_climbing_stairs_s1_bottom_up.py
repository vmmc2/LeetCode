class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ########################## BOTTOM-UP SOLUTION ###########################
        n = len(cost)
        dp = [0 for _ in range(n + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n + 1):
            total_cost_1 = dp[i - 1] if (i - 1) < 2 else dp[i - 1] + cost[i - 1]
            total_cost_2 = dp[i - 2] if (i - 2) < 2 else dp[i - 2] + cost[i - 2]
            dp[i] = min(total_cost_1, total_cost_2)

        return dp[n]
        #########################################################################