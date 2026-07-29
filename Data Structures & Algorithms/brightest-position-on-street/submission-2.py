class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        intervals = [[pos - r, pos + r] for pos, r in lights]
        intervals.sort(key=lambda x: (x[0], [1]))
        res = intervals[0][0]
        l = 0
        r = 1
        count = 1
        cur_count = 1
        cur_res = intervals[0][0]
        
        while r < len(intervals):
            while r < len(lights) and intervals[l][1] >= intervals[r][0]:
                cur_count+=1
                if cur_count > count:
                    count = cur_count
                    res = min(intervals[l][1], intervals[r][0])
                r+=1
            else:
                l+=1
            r+=1
        return res
            