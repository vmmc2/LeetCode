class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0 for i in range(len(temperatures))]

        idx = len(temperatures) - 1
        while idx >= 0:
            if len(stack) == 0:
                answer[idx] = 0
                stack.append((temperatures[idx], idx))
            else:
                while len(stack) != 0 and temperatures[idx] >= stack[-1][0]:
                    stack.pop()
                if len(stack) == 0:
                    answer[idx] = 0
                    stack.append((temperatures[idx], idx))
                else:
                    answer[idx] = stack[-1][1] - idx
                    stack.append((temperatures[idx], idx))
            idx -= 1

        return answer