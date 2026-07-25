class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in d:
                row = r + dr
                col = c + dc
                if (row in range(m)
                and col in range(n)
                and grid[row][col] > 0
                and grid[row][col] == 2147483647):
                    grid[row][col] = grid[r][c] + 1
                    q.append((row, col))
