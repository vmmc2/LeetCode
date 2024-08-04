class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        foundTarget = False
        foundRow = None

        topRow = 0
        botRow = m - 1
        while topRow <= botRow:
            midRow = (topRow + botRow) // 2
            if matrix[midRow][0] <= target and target <= matrix[midRow][n - 1]:
                foundRow = midRow
                break
            elif target < matrix[midRow][0]:
                botRow = midRow - 1
            else:
                topRow = midRow + 1

        if foundRow == None:
            return foundTarget

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[foundRow][mid] == target:
                foundTarget = True
                break
            elif matrix[foundRow][mid] > target:
                right = mid - 1
            elif matrix[foundRow][mid] < target:
                left = mid + 1

        return foundTarget
