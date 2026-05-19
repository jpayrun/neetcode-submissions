class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip = defaultdict(list)
        for pas, f, t in trips:
            trip[f].append((t, pas))
        fr = [key for key in trip.keys()]
        fr = sorted(fr)
        stop = fr[-1]
        i = 0
        heap = []
        cap = 0
        while i <= stop:
            while heap and heap[0][0] == i:
                _, pas = heapq.heappop(heap)
                cap -= pas
            res = trip[i]
            for t, pas in res:
                heapq.heappush(heap, (t, pas))
                cap+=pas
            if cap > capacity:
                return False
            i+=1
        return True
