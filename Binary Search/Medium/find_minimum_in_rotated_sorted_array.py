class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = 5001

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                minimum = min(minimum, nums[mid])
                right = mid - 1

        return minimum
