class Solution:
    def generateCombinations(self, digits, digit_to_letters, n, curr_idx, answer, curr_combination) -> None:
        if curr_idx >= n:
            answer.append(curr_combination)
            return

        curr_digit = digits[curr_idx]
        possible_letters = digit_to_letters[curr_digit]

        for letter in possible_letters:
            self.generateCombinations(digits, digit_to_letters, n, curr_idx + 1, answer, curr_combination + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        n = len(digits)
        curr_idx = 0
        curr_combination = ""

        digit_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        if len(digits) == 0:
            return []
        else:
            self.generateCombinations(digits, digit_to_letters, n, curr_idx, answer, curr_combination)
            return answer