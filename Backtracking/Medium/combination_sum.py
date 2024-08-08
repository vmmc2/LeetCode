class Solution:
    def backtrack(self, idx: int, n: int, candidates: List[int], answer: List[List[int]], current: List[int], target: int) -> None:
        if idx >= n:
            if sum(current) == target:
                answer.append(current)
            return
        if sum(current) > target:
            return
        if sum(current) == target:
            answer.append(current)
            return
    
        amountTimesCanUseCurrNum = target // candidates[idx]
        for i in range(0, amountTimesCanUseCurrNum + 1):
            self.backtrack(idx + 1, n, candidates, answer, current + ([candidates[idx]] * i), target)

        return

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        answer = []

        self.backtrack(0, n, candidates, answer, [], target)

        return answer