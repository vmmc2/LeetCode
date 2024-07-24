class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                rightOperand = stack.pop()
                leftOperand = stack.pop()
                result = None
                if token == "+":
                    result = leftOperand + rightOperand
                elif token == "-":
                    result = leftOperand - rightOperand
                elif token == "*":
                    result = leftOperand * rightOperand
                else:
                    if (leftOperand >= 0 and rightOperand > 0) or (leftOperand <= 0 and rightOperand < 0):
                        result = leftOperand // rightOperand
                    else:
                        result = (-1)*(abs(leftOperand) // abs(rightOperand))
                stack.append(result)
            else:
                stack.append(int(token))
        result = stack.pop()

        return result
