class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def helper(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = helper(n-1) + helper(n-2) + helper(n-3)
            return memo[n]
        return helper(n)