class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        def bt(r, c, i, visited):
            if i == len(word):
                return True
            for dr, dc in d:
                row = dr + r
                col = dc + c
                if row in range(m) and col in range(n) and (row, col) not in visited and board[row][col] == word[i]:
                    visited.add((row, col))
                    if bt(row, col, i+1, visited):
                        return True
                    visited.remove((row, col))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and bt(i, j, 1, {(i, j)}):
                    return True
        return False