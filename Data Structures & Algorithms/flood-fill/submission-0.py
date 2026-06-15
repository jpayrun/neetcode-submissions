class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        cl = image[sr][sc]
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set()
        def dfs(i, j):
            image[i][j] = color
            for dr, dc in d:
                row = i + dr
                col = j + dc
                if (row in range(m)
                and col in range(n)
                and (row, col) not in visit
                and image[row][col] == cl):
                    visit.add((row,col))
                    dfs(row, col)
        dfs(sr, sc)
        return image