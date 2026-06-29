class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def helper(i, j, a, b, alice = True):
            if i == j:
                return a > b
            key = (i, j, alice)
            if key in memo:
                return memo[key]
            if alice:
                a+=piles[j]
            else:
                b+=piles[j]
            back = helper(i, j-1, a, b, not alice)
            if alice:
                a+=piles[i]
            else:
                b+=piles[i]
            front = helper(i+1, j, a, b, not alice)
            memo[key] = max(back, front)
            return memo[key]
        
        return helper(0, len(piles) -1, 0, 0, True)