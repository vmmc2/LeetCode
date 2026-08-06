class Solution:
    def genParenHelper(self, parenthesis_list, curr_str, idx, length) -> None:
        if idx >= length:
            parenthesis_list.append(curr_str)
            return

        self.genParenHelper(parenthesis_list, curr_str + "(", idx + 1, length)
        self.genParenHelper(parenthesis_list, curr_str + ")", idx + 1, length)
        

    def filterValidParenHelper(self, parenthesis_list) -> None:
        answer = []

        for parenthesis in parenthesis_list:
            stack = []
            is_valid = True
            for ch in parenthesis:
                if ch == '(':
                    stack.append(ch)
                elif ch == ')' and stack:
                    stack.pop()
                else:
                    is_valid = False
                    break
            if stack:
                is_valid = False
            if is_valid:
                answer.append(parenthesis)

        return answer


    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis_list = []
        length = 2 * n

        self.genParenHelper(parenthesis_list, "", 0, length)
        answer = self.filterValidParenHelper(parenthesis_list)

        return answer
