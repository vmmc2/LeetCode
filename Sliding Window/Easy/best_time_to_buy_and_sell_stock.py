class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        left = 0
        right = 1
        n = len(prices)

        while right < n:
            currProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                answer = max(answer, currProfit)
            else:
                left = right
            right += 1
            
        return answer
