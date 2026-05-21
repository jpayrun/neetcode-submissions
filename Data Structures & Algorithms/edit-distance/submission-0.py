class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            key = (i, j)
            if key in memo:
                return memo[key]
            if word1[i] == word2[j]:
                memo[key] = helper(i+1, j+1)
            else:
                memo[key] = 1 + min(helper(i+1, j+1),
                helper(i+1, j), helper(i, j+1))
            return memo[key]
        return helper(0, 0)
            