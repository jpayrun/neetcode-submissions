"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s_ptr = 0
        e_ptr = 0
        count = 0
        while s_ptr < len(start):
            if start[s_ptr] < end[e_ptr]:
                s_ptr+=1
                count+=1
            else:
                e_ptr+=1
                count-=1
            if count > 1:
                return False
        return True
