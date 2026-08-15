class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x*x + y*y
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-dist(x, y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res