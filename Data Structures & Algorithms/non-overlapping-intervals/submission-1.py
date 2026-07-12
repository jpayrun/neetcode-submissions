class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        start = 0
        res = 0
        i = 1
        while i < len(intervals):
            if intervals[start][1] <= intervals[i][0]:
                start = i
                i += 1
            else:
                res+=1
                i+=1
        return res
