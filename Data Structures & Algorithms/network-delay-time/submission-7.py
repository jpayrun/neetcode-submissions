class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for f, to, time in times:
            graph[f].append((to, time))
        
        heap = []
        heapq.heappush(heap, (0, k))

        dist = {}

        while heap:
            t, src = heapq.heappop(heap)

            if src in dist and dist[src] <= t:
                continue
            dist[src] = t

            for dest, time in graph[src]:
                if dest not in dist or dist[dest] > time + t:
                    heapq.heappush(heap, (time + t, dest))

        if len(dist) == n:
            return max(dist.values())
        return -1
