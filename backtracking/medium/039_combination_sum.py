class Solution:
    def dfs(self, candidates, target, idx, n, curr_combination, curr_sum, answer):
        if curr_sum == target:
            answer.append(curr_combination[:])
            return
        if idx >= n or curr_sum > target:
            return

        curr_combination.append(candidates[idx])
        self.dfs(candidates, target, idx, n, curr_combination, curr_sum + candidates[idx], answer)
        curr_combination.pop()
        self.dfs(candidates, target, idx + 1, n, curr_combination, curr_sum, answer)
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)

        self.dfs(candidates, target, 0, n, [], 0, answer)

        return answer
        