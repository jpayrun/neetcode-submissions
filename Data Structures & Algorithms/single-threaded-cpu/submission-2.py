class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail = []
        pend = []
        for i, (enq, proc) in enumerate(tasks):
            heapq.heappush(avail, (enq, proc, i))
        res = []
        time = avail[0][0]
        while avail or pend:
            while avail and  avail[0][0] <= time:
                _, proc, i = heapq.heappop(avail)
                heapq.heappush(pend, (proc, i))
            if not pend:
                time = avail[0][0]
                continue
            proc, i = heapq.heappop(pend)
            time+=proc
            res.append(i)
        return res