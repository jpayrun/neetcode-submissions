class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        col = set()
        pos = set()
        neg = set()
        res = []

        def bt(row, n):
            if row == n:
                tmp = [''.join(row) for row in board]
                res.append(tmp)
                return
            for c in range(n):
                neg_val = row - c
                pos_val = row + c
                if c not in col and pos_val not in pos and neg_val not in neg:

                    col.add(c)
                    pos.add(pos_val)
                    neg.add(neg_val)
                    board[row][c] = "Q"
                    bt(row + 1, n)

                    col.remove(c)
                    pos.remove(pos_val)
                    neg.remove(neg_val)
                    board[row][c] = "."
        bt(0, n)
        return res