class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        heap = []
        for task in tasks:
            mp[task] = mp.get(task, 0) + 1
        for val in mp.values():
            heapq.heappush(heap, -val)
        q = deque()
        res = 0
        while heap or q:
            res+=1
            if heap:
                val = (-1 * heapq.heappop(heap)) - 1
                if val > 0:
                    q.append((-val, res + n))
            if q and q[0][1] == res:
                heapq.heappush(heap, q.popleft()[0])

        return res
