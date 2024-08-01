class Solution:
    def subsetGenerator(self, idx: int, n: int, nums: List[int], answer: List[int], currSet: List[int]) -> None:
        if idx >= n:
            if currSet not in answer:
                answer.append(currSet)
        else:
            self.subsetGenerator(idx + 1, n, nums, answer, currSet)
            self.subsetGenerator(idx + 1, n, nums, answer, currSet + [nums[idx]])

        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        idx = 0
        n = len(nums)
        answer = []

        nums.sort()
        self.subsetGenerator(idx, n, nums, answer, [])

        return answer
