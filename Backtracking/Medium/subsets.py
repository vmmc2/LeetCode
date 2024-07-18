class Solution:
    def generateAllSubsets(self, idx: int, n: int, currSubset: List[int], allSubsets: List[int], nums: List[int]) -> None:
        if idx == n:
            allSubsets.append(currSubset)
            return

        self.generateAllSubsets(idx + 1, n, currSubset, allSubsets, nums)
        self.generateAllSubsets(idx + 1, n, currSubset + [nums[idx]], allSubsets, nums)

        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        currSubset = []
        allSubsets = []
        idx = 0
        n = len(nums)

        self.generateAllSubsets(idx, n, currSubset, allSubsets, nums)

        return allSubsets
