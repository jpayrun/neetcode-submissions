class CountSquares:

    def __init__(self):
        self.grid = [[0] * 1001 for _ in range(1001)]
        self.points = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.grid[x][y] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            if self.grid[px][y] > 0 and self.grid[x][py] > 0:
                res += self.grid[px][y] * self.grid[x][py]
        return res
