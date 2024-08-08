class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        idx = 0
        n = len(nums)

        answer = nums[0]
        currSum = 0

        while idx <= n - 1:
            if currSum < 0: # Reset the current sum (prefix sum) if it is negative at the beginning of an iteration
                currSum = 0
            currSum += nums[idx]
            answer = max(answer, currSum)

            idx += 1
        
        return answer
