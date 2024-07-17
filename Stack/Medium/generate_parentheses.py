# Not sure if this is the optimal solution. - Runtime Complexity: O(n*(2^n))

class Solution:
    def generateCombination(self, idx: int, size: int, combination: List[str], allCombinations: List[List[str]]) -> None:
        if idx >= size:
            allCombinations.append(combination)
            return
        self.generateCombination(idx + 1, size, combination + ['('], allCombinations)
        self.generateCombination(idx + 1, size, combination + [')'], allCombinations)

        return

    def isWellFormedCombination(self, combination: List[str]) -> bool:
        stack = []
        for ch in combination:
            if ch == '(':
                stack.append(ch)
            elif ch == ')' and len(stack) == 0:
                    return False
            else:
                stack.pop()

        if len(stack) != 0:
            return False

        return True

    def generateParenthesis(self, n: int) -> List[str]:
        allCombinations = []
        idx = 0
        self.generateCombination(idx, 2*n, [], allCombinations)

        wellFormedCombinations = []

        for combination in allCombinations:
            if self.isWellFormedCombination(combination):
                wellFormedCombinations.append("".join(combination))

        return wellFormedCombinations
