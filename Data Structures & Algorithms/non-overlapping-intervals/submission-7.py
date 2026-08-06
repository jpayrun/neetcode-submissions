class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ints = sorted(intervals, key = lambda x: x[1])

        l = 0
        res = 0
        for i in range(1, len(ints)):
            if ints[l][1] > ints[i][0]:
                res+=1
            else:
                l = i
        return res