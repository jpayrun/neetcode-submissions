class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        def eat(n, speed):
            return math.ceil(n / speed)
        while l <= r:
            m = (l + r) // 2
            tot = 0
            for pile in piles:
                tot += eat(pile, m)
            if tot <= h:
                r = m - 1
            else:
                l = m + 1
        return l

        