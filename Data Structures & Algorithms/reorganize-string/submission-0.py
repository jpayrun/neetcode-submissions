class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = {}
        for c in s:
            mp[c] = mp.get(c, 0) + 1
        maxHeap = [(-cnt, char) for char, cnt in mp.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = (cnt, char)
        return res
        