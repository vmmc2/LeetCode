class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height) - 1

        while(left < right):
            containerHeight = min(height[left], height[right])
            containerWidth = right - left
            answer = max(answer, containerHeight * containerWidth)
            if(height[left] <= height[right]):
                left += 1
            else:
                right -= 1

        return answer
