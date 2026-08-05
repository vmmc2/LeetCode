class Solution:
    def dfs(self, grid: List[List[int]], visited: List[List[int]], m: int, n: int, x: int, y: int):
        visited[x][y] = 1
        area = 1

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and grid[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                area += self.dfs(grid, visited, m, n, new_x, new_y)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for j in range(n)] for i in range(m)]
        answer = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = self.dfs(grid, visited, m, n, i, j)
                    answer = max(answer, area)

        return answer
