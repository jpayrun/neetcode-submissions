class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def helper(i, tot, amount):
            key = (i, tot)
            if (i, tot) in memo:
                return memo[key]
            if tot == amount:
                return 0
            if tot > amount:
                return amount + 1
            if i == len(coins):
                return amount + 1
            take = helper(i, tot+coins[i], amount) + 1
            skip = helper(i+1, tot, amount)
            memo[key] = min(take, skip)
            return memo[key]
        res = helper(0, 0, amount)
        return res if res <= amount else -1