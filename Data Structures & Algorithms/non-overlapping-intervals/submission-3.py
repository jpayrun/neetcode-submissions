class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ints = sorted(intervals, key = lambda x: x[1])

        start = 0
        res = 0

        for i in range(1, len(ints)):
            if ints[start][1] <= ints[i][0]:
                start = i
            else:
                res+=1

        return res
