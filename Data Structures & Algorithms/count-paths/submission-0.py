class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]
            if i == m and j == n:
                return 1
            if i > m or j > n:
                return 0
            memo[key] = dfs(i+1, j) + dfs(i, j+1)
            return memo[key]
        return dfs(1, 1)