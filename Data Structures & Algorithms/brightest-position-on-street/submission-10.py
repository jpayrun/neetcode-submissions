class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)

        for p, r in lights:
            s = p - r
            e = p + r
            
            diff[s]+=1
            diff[e+1]-=1
        
        max_bright = cur = 0
        res = -float('inf')

        for key in sorted(diff.keys()):
            cur+=diff[key]
            if cur > max_bright:
                max_bright = cur
                res = key
        return res