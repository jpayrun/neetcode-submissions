class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            key = (i, j)
            if key in memo:
                return memo[key]
            res = False
            if i < len(s1) and s1[i] == s3[i + j]:
                res = dfs(i + 1, j) or res
            if j < len(s2) and s2[j] == s3[i + j]:
                res = dfs(i, j + 1) or res
            memo[key] = res
            return memo[key]
        return dfs(0, 0)