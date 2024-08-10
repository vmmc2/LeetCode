class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Calculate the transposed matrix.
        # Reverse each row.
        m = len(matrix) # num rows
        n = len(matrix[0]) # num cols

        for i in range(0, m):
            for j in range(0, n):
                if i < j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        for i in range(0, m):
            matrix[i].reverse()

        return
