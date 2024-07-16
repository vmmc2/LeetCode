class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            current_freq = freq.get(num, 0)
            freq[num] = current_freq + 1
            if(freq[num] > 1):
                return True

        return False
