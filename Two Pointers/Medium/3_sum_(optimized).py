class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        
        for i in range(0, n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left  - 1]:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1

        return answer
