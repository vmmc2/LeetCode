class Solution:
    def generateSubsets(self, nums: List[int], to_include: List[bool], idx: int, n: int, answer: List[List[int]]) -> None:
        if idx >= n:
            subset = []
            for i in range(len(to_include)):
                if to_include[i]:
                    subset.append(nums[i])
            answer.append(subset)
            return

        self.generateSubsets(nums, to_include + [True], idx + 1, n, answer)
        self.generateSubsets(nums, to_include + [False], idx + 1, n, answer)

        return


    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        idx = 0

        self.generateSubsets(nums, [True], idx + 1, n, answer)
        self.generateSubsets(nums, [False], idx + 1, n, answer)

        return answer
        