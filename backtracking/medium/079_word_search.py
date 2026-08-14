class Solution:
    def dfs(self, board, visited, word, curr_idx, m, n, x, y) -> bool:
        if curr_idx == len(word) - 1:
            return True

        visited[x][y] = True

        dx = [1, -1, 0,  0]
        dy = [0,  0, 1, -1]

        found_answer = False
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y] and board[new_x][new_y] == word[curr_idx + 1]:
                found_answer = found_answer or self.dfs(board, visited, word, curr_idx + 1, m, n, new_x, new_y)

        visited[x][y] = False
        
        return found_answer

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        start_letter = word[0]

        for i in range(m):
            for j in range(n):
                if board[i][j] == start_letter:
                    visited = [[False for j in range(n)] for i in range(m)]
                    found_answer = self.dfs(board, visited, word, 0, m, n, i, j)
                    if found_answer:
                        return True
        
        return False
