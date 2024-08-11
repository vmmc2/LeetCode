class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(0, amount + 1)] # dp[i] -> minimum amount of coins I need to achieve the value i.
        dp[0] = 0

        coins.sort()
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i: # The value of the current coin is bigger than the amount "i" I'm trying to achieve. 
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float("inf") else -1
