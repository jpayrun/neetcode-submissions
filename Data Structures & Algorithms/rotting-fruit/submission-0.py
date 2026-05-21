class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    q.append((i, j))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0
        while q and fresh:
            res+=1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc in directions:
                    row, col = dr + i, dc + j
                    if (row in range(m)
                    and col in range(n)
                    and grid[row][col] == 1):
                        q.append((row, col))
                        fresh-=1
                        grid[row][col] = 2
        return res if fresh == 0 else -1