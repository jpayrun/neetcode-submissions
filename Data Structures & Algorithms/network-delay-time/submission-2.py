class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph = {}
        # for src, node, time in times:
        #     if src in graph:
        #         graph[src].append((node, time))
        #     else:
        #         graph[src] = [(node, time)]
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        dist = {}
        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue
            dist[node] = time

            for neigh, weight in graph[node]:
                if neigh not in dist:
                    heapq.heappush(heap, (weight + time, neigh))
        print(dist)
        if len(dist) != n:
            return -1
        return max(dist.values())