class Solution:
    def dfs(self, heights: List[List[int]], visited: List[List[bool]], achievable: List[List[int]], m: int, n: int, x: int, y: int) -> None:
        visited[x][y] = True
        achievable[x][y] += 1

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and visited[new_x][new_y] == False and heights[new_x][new_y] >= heights[x][y]:
                self.dfs(heights, visited, achievable, m, n, new_x, new_y)


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        answer = []

        # Instead of executing the DFS from each cell of the grid, execute the DFS
        # from the borders of the island and then perform a traversal, checking which cells
        # were able to be achieved more than once.
        achievable_pacific = [[0 for j in range(n)] for i in range(m)]
        achievable_atlantic = [[0 for j in range(n)] for i in range(m)]

        # Dealing with first row
        for y in range(n):
            visited = [[False for j in range(n)] for i in range(m)]
            self.dfs(heights, visited, achievable_pacific, m, n, 0, y)

        # Dealing with first column
        for x in range(m):
            visited = [[False for j in range(n)] for i in range(m)]
            self.dfs(heights, visited, achievable_pacific, m, n, x, 0)

        for i in range(m):
            for j in range(n):
                if achievable_pacific[i][j] > 0:
                    achievable_pacific[i][j] = 1

        # Dealing with last row
        for y in range(n):
            visited = [[False for j in range(n)] for i in range(m)]
            self.dfs(heights, visited, achievable_atlantic, m, n, m - 1, y)

        # Dealing with last column
        for x in range(m):
            visited = [[False for j in range(n)] for i in range(m)]
            self.dfs(heights, visited, achievable_atlantic, m, n, x, n - 1)

        for i in range(m):
            for j in range(n):
                if achievable_atlantic[i][j] > 0:
                    achievable_atlantic[i][j] = 1

        for i in range(m):
            for j in range(n):
                if achievable_pacific[i][j] and achievable_atlantic[i][j]:
                    answer.append([i, j])

        return answer          
