class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(-num)
        heapq.heapify(heap)
        i = 0
        res = 0
        while i < k:
            res = heapq.heappop(heap)
            i+=1
        return -res