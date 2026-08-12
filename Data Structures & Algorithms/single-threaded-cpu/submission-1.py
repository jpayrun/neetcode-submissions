class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail = []
        pend = []
        for i, (enq, pros) in enumerate(tasks):
            heapq.heappush(avail, (enq, pros, i))
        time = avail[0][0]
        res = []
        while avail or pend:
            while avail and time >= avail[0][0]:
                t, pros, i = heapq.heappop(avail)
                heapq.heappush(pend, (pros, i))
            if not pend:
                time = avail[0][0]
                continue
            pros, i = heapq.heappop(pend)
            time+=pros
            res.append(i)
        return res