class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = [str(i) for i in range(1, 10)]

        # Checking each row
        for i in range(0, len(board)):
            freq = { }
            for j in range(0, len(board)):
                if(board[i][j] in digits):
                    freq[board[i][j]] = freq.get(board[i][j], 0) + 1
                    if(freq[board[i][j]] > 1):
                        return False

        # Checking each column
        for i in range(0, len(board)):
            freq = { }
            for j in range(0, len(board)):
                if(board[j][i] in digits):
                    freq[board[j][i]] = freq.get(board[j][i], 0) + 1
                    if(freq[board[j][i]] > 1):
                        return False

        # Checking each 3x3 sub-grid
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                freq = { }
                for x in range(0, 3):
                    for y in range(0, 3):
                        if(board[i + x][j + y] in digits):
                            freq[board[i + x][j + y]] = freq.get(board[i + x][j + y], 0) + 1
                            if(freq[board[i + x][j + y]] > 1):
                                return False

        return True
