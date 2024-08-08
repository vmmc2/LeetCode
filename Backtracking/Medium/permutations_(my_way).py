class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(current: List[int], numsLeft: List[int]) -> None:
            if len(numsLeft) == 0:
                answer.append(current)
                return

            for i in range(len(numsLeft)):
                backtrack(current + [numsLeft[i]], numsLeft[:i] + numsLeft[i+1:])

            return

        backtrack([], nums)

        return answer
