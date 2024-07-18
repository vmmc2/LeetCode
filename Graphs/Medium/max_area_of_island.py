class Solution:
    def dfs(self, row: int, col: int, grid: List[List[int]], visited: List[List[bool]], m: int, n: int, currentArea: List[int]) -> None:
        visited[row][col] = True
        currentArea[0] += 1

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        for i in range(0, 4):
            newRow = row + dx[i]
            newCol = col + dy[i]
            if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and grid[newRow][newCol] == 1 and not visited[newRow][newCol]:
                self.dfs(newRow, newCol, grid, visited, m, n, currentArea)

        return

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0

        visited = [[False for j in range(0, n)] for i in range(0, m)]

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1 and not visited[i][j]:
                    currentArea = [0]
                    self.dfs(i, j, grid, visited, m, n, currentArea)
                    maxArea = max(maxArea, currentArea[0])

        return maxArea
