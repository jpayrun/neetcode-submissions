class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s_ptr = 0
        e_ptr = 0
        res = 0
        count = 0
        while s_ptr < len(start):
            if start[s_ptr] < end[e_ptr]:
                s_ptr+=1
                count+=1
            else:
                e_ptr+=1
                count-=1
            res = max(count, res)
        return res