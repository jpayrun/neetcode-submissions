class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            key = (i, j)
            if j == 0 and i == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if key in memo:
                return memo[key]
            memo[key] = dfs(i-1, j) + dfs(i, j-1)
            return memo[key]
        return dfs(m-1, n-1)
