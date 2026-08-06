class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def backtrack(currIdx, currSubset, total) -> None:
            if total == target:
                answer.append(currSubset.copy())
                return
            if (total > target) or (currIdx == len(candidates)):
                return

            # Include 'candidates[i]'
            currSubset.append(candidates[currIdx])
            backtrack(currIdx + 1, currSubset, total + candidates[currIdx])
            currSubset.pop()

            # Don't include 'candidates[i]'
            while currIdx + 1 < len(candidates) and candidates[currIdx] == candidates[currIdx + 1]:
                currIdx += 1
            backtrack(currIdx + 1, currSubset, total)


        backtrack(0, [], 0)

        return answer