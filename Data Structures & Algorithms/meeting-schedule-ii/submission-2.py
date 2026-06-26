class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        s_ptr = 0
        e_ptr = 0
        res = 0
        count = 0
        while s_ptr < len(starts):
            if starts[s_ptr] < ends[e_ptr]:
                count += 1
                s_ptr += 1
            else:
                count -= 1
                e_ptr += 1
            res = max(res, count)
            
        return res