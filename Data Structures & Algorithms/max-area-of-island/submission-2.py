class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        def area(r, c):
            grid[r][c] = 0
            res = 1
            d = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr, dc in d:
                row = dr + r
                col = dc + c
                if row in range(m) and col in range(n) and grid[row][col] == 1:
                    res = area(row, col) + res
            return res
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, area(i, j))
        return res