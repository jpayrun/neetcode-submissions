class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = sorted(people)
        res = 0
        l = 0
        r = len(p) - 1
        while l <= r:
            if p[l] + p[r] <= limit:
                l+=1
            res+=1
            r-=1
        return res