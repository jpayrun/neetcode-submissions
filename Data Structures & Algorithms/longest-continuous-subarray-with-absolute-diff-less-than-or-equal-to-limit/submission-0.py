class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = []
        maxq = []
        res = i = 0
        for j, n in enumerate(nums):
            heapq.heappush(minq, (n, j))
            heapq.heappush(maxq, (-n, j))
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res