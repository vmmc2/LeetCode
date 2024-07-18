class Solution:
    def dfs(self, row: int, col: int, grid: List[List[int]], visited: List[List[bool]], n: int, m: int) -> None:
        visited[row][col] = True

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        for i in range(0, 4):
            newRow = row + dx[i]
            newCol = col + dy[i]
            if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m and grid[newRow][newCol] == '1' and not visited[newRow][newCol]:
                self.dfs(newRow, newCol, grid, visited, n, m)

        return

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        numberIslands = 0

        visited = [[False for j in range(m)] for i in range(n)]

        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == '1' and not visited[i][j]:
                    numberIslands += 1
                    self.dfs(i, j, grid, visited, n, m)

        return numberIslands
