class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set()
        res = 0
        while heap:
            t, r, c = heapq.heappop(heap)
            res = max(t, res)
            if r == n - 1 and c == n - 1:
                return res
            visited.add((r, c))

            for dr, dc in d:
                row = dr + r
                col = dc + c
                if row in range(n) and col in range(n):
                    if (row, col) in visited:
                        continue
                    heapq.heappush(heap, (grid[row][col], row, col))

        