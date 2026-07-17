class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        heap = []
        for t in tasks:
            mp[t] = mp.get(t, 0) + 1 
        for val in mp.values():
            heapq.heappush(heap, -val)
        q = deque()
        res = 0
        while heap or q:
            res+=1
            if heap:
                val = heapq.heappop(heap)
                if val + 1 < 0:
                    q.append((val + 1, n + res))
            if q and q[0][1] == res:
                heapq.heappush(heap, q.popleft()[0])
        return res
