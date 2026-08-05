class Solution:
    def checkFill(self, board, visited, shouldBeFilled, m, n, x, y) -> None:
        visited[x][y] = True
        shouldBeFilled[x][y] = False

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O' and not visited[new_x][new_y]:
                self.checkFill(board, visited, shouldBeFilled, m, n, new_x, new_y)

        return
        

    def fill(self, board, visited, shouldBeFilled, m, n, x, y) -> None:
        visited[x][y] = True
        board[x][y] = 'X'
        shouldBeFilled[x][y] = False

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O' and shouldBeFilled[x][y] and not visited[new_x][new_y]:
                self.fill(board, visited, shouldbeFilled, m, n, new_x, new_y)

        return


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        shouldBeFilled = [[True for j in range(n)] for i in range(m)]
        visited = [[False for j in range(n)] for i in range(m)]
        # Checking first row
        for j in range(n):
            if board[0][j] == 'O' and not visited[0][j]:
                self.checkFill(board, visited, shouldBeFilled, m, n, 0, j)
        # Checking last row
        for j in range(n):
            if board[m - 1][j] == 'O' and not visited[m - 1][j]:
                self.checkFill(board, visited, shouldBeFilled, m, n, m - 1, j)
        # Checking first column
        for i in range(m):
            if board[i][0] == 'O' and not visited[i][0]:
                self.checkFill(board, visited, shouldBeFilled, m, n, i, 0)
        # Checking last column
        for i in range(m):
            if board[i][n - 1] == 'O' and not visited[i][n - 1]:
                self.checkFill(board, visited, shouldBeFilled, m, n, i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    shouldBeFilled[i][j] = False

        visited = [[False for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and shouldBeFilled[i][j] and not visited[i][j]:
                    self.fill(board, visited, shouldBeFilled, m, n, i, j)

        return
