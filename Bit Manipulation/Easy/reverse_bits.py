class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0

        for i in range(0, 32):
            if n & 1 == 1:
                answer = answer | 1
            if i == 31:
                break
            answer = answer << 1
            n = n >> 1


        return answer
