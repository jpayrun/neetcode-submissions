class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0
        for a in range(amount + 1):
            for coin in coins:
                if a - coin >= 0 and memo[a - coin] < float('inf'):
                    memo[a] = min(memo[a], 1 + memo[a - coin])
        return memo[amount] if memo[amount] < float('inf') else -1