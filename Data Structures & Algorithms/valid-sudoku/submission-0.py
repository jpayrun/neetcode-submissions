class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            vals = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in vals:
                    return False
                vals.add(board[i][j])
        for j in range(n):
            vals = set()
            for i in range(m):
                if board[i][j] == ".":
                    continue
                if board[i][j] in vals:
                    return False
                vals.add(board[i][j])
        for i in range(3):
            for j in range(3):
                vals = set()
                for row in range(3):
                    for col in range(3):
                        if board[3 * i + row][3 * j + col] == ".":
                            continue
                        if board[3 * i + row][3 * j + col] in vals:
                            return False
                        vals.add(board[3 * i + row][3 * j + col])
        return True