class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums) # We initially assume that the answer is the subarray of size 1 with the largest value.
        currMin, currMax = 1, 1

        n = len(nums)

        for i in range(0, n):
            if nums[i] == 0:
                currMin, currMax = 1, 1 # Must reset these values so it does not contaminate the solution
                continue
            
            temp = currMax * nums[i]
            currMax = max(currMax * nums[i], currMin * nums[i], nums[i])
            currMin = min(temp, currMin * nums[i], nums[i])

            answer = max(answer, currMax)
        
        return answer
