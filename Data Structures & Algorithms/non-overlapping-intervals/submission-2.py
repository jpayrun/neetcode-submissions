class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        start = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[start][1] <= intervals[i][0]:
                start = i
            else:
                res+=1
        return res
