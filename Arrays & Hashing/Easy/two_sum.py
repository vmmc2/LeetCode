class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = {}

        for i in range(0, len(nums)):
            needed_value = target - nums[i]
            if needed_value in idx_dict:
                return [i, idx_dict[needed_value]]
            idx_dict[nums[i]] = i