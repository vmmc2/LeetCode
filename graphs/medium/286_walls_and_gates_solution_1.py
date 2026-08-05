# Time Complexity: O(M^2 * N^2)

from collections import deque

class Solution:
    def bfs(self, grid, visited, m, n, x, y) -> None:
        visited[x][y] = True

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        queue = deque()
        queue.append((x, y))

        while len(queue) != 0:
            x_curr, y_curr = queue.popleft()
            for i in range(4):
                x_new = x_curr + dx[i]
                y_new = y_curr + dy[i]
                if 0 <= x_new < m and 0 <= y_new < n and not visited[x_new][y_new] and grid[x_new][y_new] > grid[x_curr][y_curr] + 1:
                    queue.append((x_new, y_new))
                    visited[x_new][y_new] = True
                    grid[x_new][y_new] = grid[x_curr][y_curr] + 1

        return
            

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        treasure_coords = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasure_coords.append((i, j))

        
        for treasure_coord in treasure_coords:
            x, y = treasure_coord
            visited = [[False for j in range(n)] for i in range(m)]
            self.bfs(grid, visited, m, n, x, y)

        return
