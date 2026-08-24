class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hold = []
        heap = []
        for i, (p, c) in enumerate(zip(profits, capital)):
            heapq.heappush(heap, (-p, c, i))
        j = 0
        while j < k:
            if not heap:
                return w
            p, c, i = heapq.heappop(heap)
            if c <= w:
                w+=-p
                j+=1
                while hold:
                    heapq.heappush(heap, hold.pop())
            else:
                hold.append((p, c, i))
        return w
