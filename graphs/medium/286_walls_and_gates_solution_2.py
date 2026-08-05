# This solution uses a technique called Multi-Source BFS
# We initialize our queue with all nodes of interest and already
# mark them as visited. Then, we just run the BFS algorithm as
# we are already used to.
# Time Complexity: O(M * N)

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        visited = [[False for j in range(n)] for i in range(m)]
        treasure_coords = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    treasure_coords.append((i, j))
                    visited[i][j] = True

        queue = deque()
        queue.extend(treasure_coords)

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        while len(queue) != 0:
            x_curr, y_curr = queue.popleft()
            for i in range(4):
                x_new = x_curr + dx[i]
                y_new = y_curr + dy[i]
                if 0 <= x_new < m and 0 <= y_new < n and not visited[x_new][y_new] and grid[x_new][y_new] != -1:
                    queue.append((x_new, y_new))
                    visited[x_new][y_new] = True
                    grid[x_new][y_new] = grid[x_curr][y_curr] + 1 

        return
