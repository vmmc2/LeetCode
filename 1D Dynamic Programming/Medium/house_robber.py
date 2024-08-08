class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxAmount = [0 for i in range(n)]

        for i in range(n):
            if i == 0:
                maxAmount[i] = nums[i]
            elif i == 1:
                maxAmount[i] = max(nums[i], nums[i - 1])
            else:
                maxAmount[i] = max(maxAmount[i - 1], maxAmount[i - 2] + nums[i])

        return maxAmount[n - 1]
