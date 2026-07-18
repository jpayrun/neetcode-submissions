class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        vis = set()
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        def bt(r, c, i, vis):
            if i == len(word):
                return True
            for dr, dc in d:
                row = r + dr
                col = c + dc
                if (row in range(m)
                and col in range(n)
                and (row, col) not in vis
                and word[i] == board[row][col]):
                    vis.add((row, col))
                    if bt(row, col, i+1, vis):
                        return True
                    vis.remove((row, col))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis.add((i, j))
                    if bt(i, j, 1, vis):
                        return True
                    vis.remove((i, j))
        return False