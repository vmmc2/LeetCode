class Solution:
    def rob(self, nums: List[int]) -> int:
        ################################# BOTTOM-UP SOLUTION #################################
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            n = len(nums)
            dp = [0 for _ in range(n)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

            return dp[n - 1]
        #######################################################################################
