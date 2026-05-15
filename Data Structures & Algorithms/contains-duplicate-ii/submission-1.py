class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0,
        r = len(nums) - 1
        memo = {}
        res = False
        for i, num in enumerate(nums):
            if num in memo:
                res = max(res, abs(memo[num] - i) <= k)
                memo[num] = i
            else:
                memo[num] = i
        return res