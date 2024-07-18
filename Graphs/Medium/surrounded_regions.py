from collections import deque

class Solution:
    def isEnclosedRegion(self, row: int, col: int, grid: List[List[str]], visited: List[List[bool]], m: int, n: int) -> bool:
        queue = deque()
        answer = [True, [ ]] # Suppose that the region is enclosed
        visited[row][col] = True
        answer[1].append([row, col])
        queue.append((row, col))
        
        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        while len(queue) != 0:
            currCell = queue.popleft()
            for i in range(4):
                newRow = currCell[0] + dx[i]
                newCol = currCell[1] + dy[i]
                if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and grid[newRow][newCol] == 'O' and not visited[newRow][newCol]:
                    if newRow == 0 or newRow == m - 1 or newCol == 0 or newCol == n - 1:
                        answer[0] = False
                    visited[newRow][newCol] = True
                    answer[1].append([newRow, newCol])
                    queue.append((newRow, newCol)) 

        return answer

    def fill(self, board: List[List[str]], cellsToFill: List[List[int]]) -> None:
        for cell in cellsToFill:
            board[cell[0]][cell[1]] = 'X' 

        return

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]

        for i in range(m):
            if i == 0 or i == m - 1:
                continue
            for j in range(n):
                if j == 0 or j == n - 1:
                    continue
                if board[i][j] == 'O' and not visited[i][j]:
                    answer = self.isEnclosedRegion(i, j, board, visited, m, n)
                    if answer[0]:
                        self.fill(board, answer[1])
        return
