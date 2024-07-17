class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []

        for i in range(0, n):
            if s[i] in [ '(', '{', '[' ]:
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0: return False
                if stack[-1] != '(': return False
                stack.pop()
            elif s[i] == '}':
                if len(stack) == 0: return False
                if stack[-1] != '{': return False
                stack.pop()
            elif s[i] == ']':
                if len(stack) == 0: return False
                if stack[-1] != '[': return False
                stack.pop()

        if len(stack) != 0:
            return False

        return True
