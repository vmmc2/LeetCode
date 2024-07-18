from collections import deque

class Solution:
    def bfs(self, row: int, col: int, grid: List[List[int]], distance: List[List[int]], visited: List[List[bool]], m: int, n: int) -> None:
        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        distance[row][col] = 0
        visited[row][col] = 1

        queue = deque()
        queue.append((row, col))

        while len(queue) != 0:
            currCell = queue.popleft()
            for i in range(4):
                newRow = currCell[0] + dx[i] 
                newCol = currCell[1] + dy[i]
                if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and grid[newRow][newCol] > 0 and visited[newRow][newCol] == False:
                    queue.append((newRow, newCol))
                    visited[newRow][newCol] = True
                    distance[newRow][newCol] = 1 + distance[currCell[0]][currCell[1]]

        return
 
    def updateFinalDistance(self, finalDistance: List[List[int]], distance: List[List[int]], m: int, n: int) -> None:
        for i in range(m):
            for j in range(n):
                finalDistance[i][j] = min(finalDistance[i][j], distance[i][j])

        return 

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        finalDistance =  [[99999 for j in range(n)] for i in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2: # Rotten orange. Need to run a BFS from it.
                    visited = [[False for j in range(n)] for i in range(m)]
                    distance =  [[99999 for j in range(n)] for i in range(m)]
                    self.bfs(i, j, grid, distance, visited, m, n)
                    self.updateFinalDistance(finalDistance, distance, m, n)

        maxMinutes = 0    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and finalDistance[i][j] == 99999:
                    return -1
                elif grid[i][j] == 1 and finalDistance[i][j] != 99999:
                    maxMinutes = max(maxMinutes, finalDistance[i][j])

        return maxMinutes
