class Solution:
    def generateSubset(self, answer, subsets, nums, n, currIdx, currSubset) -> None:
        if currIdx >= n:
            subsetAsTuple = tuple(currSubset)
            if subsetAsTuple not in subsets:
                subsets.add(subsetAsTuple)
            return

        self.generateSubset(answer, subsets, nums, n, currIdx + 1, currSubset + [nums[currIdx]])
        self.generateSubset(answer, subsets, nums, n, currIdx + 1, currSubset)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        subsets = set()
        n = len(nums)

        self.generateSubset(answer, subsets, nums, n, 0, [])
        self.generateSubset(answer, subsets, nums, n, 0, [])

        for subset in subsets:
            answer.append(list(subset))

        return answer