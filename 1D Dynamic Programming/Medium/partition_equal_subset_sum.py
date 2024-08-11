class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSetSum = sum(nums)
        targetSum = totalSetSum / 2

        possibleSubsetSums = set()
        n = len(nums)

        idx = n - 1

        while idx >= 0:
            if idx == n - 1:
                possibleSubsetSums.add(0) # The empty subset case
                possibleSubsetSums.add(nums[idx]) # The subset with just the last element
            else:
                nextSubsetSums = []

                for subsetSum in possibleSubsetSums:
                    nextSubsetSums.append(subsetSum + nums[idx])

                for currSubsetSum in nextSubsetSums:
                    possibleSubsetSums.add(currSubsetSum)
            idx -= 1

        return targetSum in possibleSubsetSums
