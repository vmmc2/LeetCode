# Again, this is a question that involves using the concept of
# Multi-Source BFS.

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = [[False for j in range(n)] for i in range(m)]
        time = [[999999 for j in range(n)] for i in range(m)]
        queue = deque()

        rotten_orange_coords = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_orange_coords.append((i, j))
                    visited[i][j] = True
                    time[i][j] = 0
                elif grid[i][j] == 0:
                    time[i][j] = 0

        queue.extend(rotten_orange_coords)

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        while len(queue) != 0:
            x_curr, y_curr = queue.popleft()
            for i in range(4):
                x_new = x_curr + dx[i]
                y_new = y_curr + dy[i]
                if 0 <= x_new < m and 0 <= y_new < n and not visited[x_new][y_new] and grid[x_new][y_new] == 1:
                    queue.append((x_new, y_new))
                    visited[x_new][y_new] = True
                    time[x_new][y_new] = time[x_curr][y_curr] + 1

        answer = 0

        for i in range(m):
            for j in range(n):
                answer = max(answer, time[i][j])

        return answer if answer != 999999 else -1
        