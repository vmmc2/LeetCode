class Solution:
    def change(self, n: int) -> int:
        answer = 0
        n = str(n)
        for digit in n:
            answer += (int(digit) ** 2)
        
        return answer

    def isHappyNumber(self, n: int) -> bool:
        return n == 1
        
    def isHappy(self, n: int) -> bool:
        seenNumbers = set()
        isHappyNumber = False

        while not isHappyNumber:
            if self.isHappyNumber(n):
                break
            if n in seenNumbers: # We are in a loop.
                return False
            seenNumbers.add(n)
            n = self.change(n)
        
        return True
