class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heapq.heappush(heap, (-a, 'a'))
        if b:
            heapq.heappush(heap, (-b, 'b'))
        if c:
            heapq.heappush(heap, (-c, 'c'))
        hold = None
        res = ""
        while heap or hold:
            if not heap:
                return res
            i, char = heapq.heappop(heap)
            if len(res) >= 2 and (res[-1] == char and res[-2] == char):
                hold = (i, char)
                continue
            res += char
            if i + 1 != 0:
                heapq.heappush(heap, (i + 1, char))
            if hold:
                heapq.heappush(heap, hold)
                hold = None

        return res