class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(i, j):
            grid[i][j] = 0
            area = 1
            for dr, dc in directions:
                row, col = dr+i, dc+j
                if (row in range(n)
                and col in range(m)
                and grid[row][col] == 1):
                    area+=dfs(row, col)
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
        return res