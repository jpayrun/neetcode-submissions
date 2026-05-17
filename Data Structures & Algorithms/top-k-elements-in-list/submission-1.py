class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for num in nums:
            if num in memo:
                memo[num] += 1
            else:
                memo[num] = 1
        heap = []
        for key in memo:
            heapq.heappush(heap, (memo[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
