class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r, c):
            area = 1
            grid[r][c] = 0
            for dr, dc in d:
                row = r + dr
                col = c + dc
                if row in range(m) and col in range(n) and grid[row][col] == 1:
                    
                    area+=dfs(row, col)
            return area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res