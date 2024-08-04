class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        n = len(nums)

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                break
            if nums[left] <= nums[mid]: # First half is sorted
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]: # Second half is sorted
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return index
