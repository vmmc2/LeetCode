class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        expectedSum = n*(n + 1)//2
        givenSum = sum(nums)

        answer = expectedSum - givenSum
        return answer
