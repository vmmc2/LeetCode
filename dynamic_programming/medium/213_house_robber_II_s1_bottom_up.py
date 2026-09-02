class Solution:
    def robAux(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            n = len(nums)

            dp_result_first_house = self.robAux(nums[:n - 1])
            dp_result_last_house = self.robAux(nums[1:])

            return max(dp_result_first_house, dp_result_last_house)
