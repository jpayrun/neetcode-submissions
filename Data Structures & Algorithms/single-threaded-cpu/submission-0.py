class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail = []
        pending = []
        for i, (enq, pros) in enumerate(tasks):
            heapq.heappush(pending, (enq, pros, i))
        time = 0
        res = []
        while pending or avail:
            while pending and pending[0][0] <= time:
                enq, pros, i = heapq.heappop(pending)
                heapq.heappush(avail, (pros, i))
            if not avail:
                time = pending[0][0]
                continue
            
            processTime, i = heapq.heappop(avail)
            time += processTime
            res.append(i)
        return res