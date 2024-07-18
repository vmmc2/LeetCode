class Solution:
    def auxRob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]

        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i - 1], nums[i])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            maxAmount1 = self.auxRob(nums[1:])
            maxAmount2 = self.auxRob(nums[:n-1])
            return max(maxAmount1, maxAmount2)
