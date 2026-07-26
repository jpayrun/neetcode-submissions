class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r:
            m = l + (r - l) // 2
            tot = 0
            for pile in piles:
                tot += math.ceil(pile / m)
            if tot > h:
                l = m + 1
            else:
                r = m
        return l

        