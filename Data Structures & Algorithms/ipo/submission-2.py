class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        minHeap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minHeap)

        for i in range(k):
            while minHeap and minHeap[0][0] <= w:
                heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap)[1])
            if not maxHeap:
                break
            w+=-1 * heapq.heappop(maxHeap)
        return w