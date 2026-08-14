class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]

        curr_permutations = []
        permutations = self.permute(nums[1:])
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                p = permutation.copy()
                p.insert(i, nums[0])
                curr_permutations.append(p)

        return curr_permutations
