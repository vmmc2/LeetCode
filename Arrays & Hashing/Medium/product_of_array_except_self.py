# Non-Optimal Solution - Runtime Complexity: O(n²)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1 for i in range(0, n)]

        for i in range(0, n):
            product = 1
            for j in range(0, n):
                if i != j:
                    product *= nums[j]
            answer[i] = product

        return answer

