class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for num in nums:
            if num in memo:
                memo[num] += 1
            else:
                memo[num] = 1
        values = dict(sorted(memo.items(), key=lambda x: x[1], reverse=True)).keys()
        res = []
        for val in values:
            res.append(val)
        return res[:k]