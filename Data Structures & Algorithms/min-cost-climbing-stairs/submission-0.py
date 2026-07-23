class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * n
        def helper(i):
            if i <= 0:
                return 0
            if dp[i] < float('inf'):
                return dp[i]
            dp[i] = min(cost[i] + helper(i - 1), cost[i-1] + helper(i - 2))
            return dp[i]
        return helper(len(cost) -1)
