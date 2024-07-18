import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1 # lower bound
        right = piles[-1] # upper bound

        k = right
        while left <= right:
            current_k = (left + right) // 2
            current_h = 0
            for i in range(0, len(piles)):
                if current_k >= piles[i]:
                    current_h += 1
                else:
                    current_h += math.ceil(piles[i]/current_k)
            if current_h > h:
                left = current_k + 1
            elif current_h <= h:
                k = current_k
                right = current_k - 1
        
        return k
