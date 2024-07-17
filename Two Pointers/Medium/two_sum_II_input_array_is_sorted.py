class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        answer = []

        while(left < right):
            if(numbers[left] + numbers[right] == target):
                answer = [left + 1, right + 1]
                break
            elif(numbers[left] + numbers[right] < target):
                left += 1
            else:
                right -= 1

        return answer
