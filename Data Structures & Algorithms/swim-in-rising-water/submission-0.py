class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        res = 0
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        while heap:
            l, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            res = max(res, l)
            if i == m - 1 and j == n - 1:
                return res
            for dr, dc in d:
                row = i + dr
                col = j + dc
                if row in range(m) and col in range(n):
                    if (row, col) in visited:
                        continue
                    heapq.heappush(heap, (grid[row][col], row, col))