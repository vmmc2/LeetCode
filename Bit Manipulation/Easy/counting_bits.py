class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []

        for i in range(0, n + 1):
            curr = i
            currAnswer = 0
            while curr != 0:
                if curr & 1 == 1:
                    currAnswer += 1
                curr = curr >> 1

            answer.append(currAnswer)
            
        return answer
