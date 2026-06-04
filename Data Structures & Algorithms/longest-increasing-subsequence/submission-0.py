class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def helper(i, t=-1001):
            key = (i, t)
            if i == len(nums):
                return 0
            if key in memo:
                return memo[key]
            skip = helper(i+1, t)
            if nums[i] > t:
                take = 1 + helper(i+1, nums[i])
                memo[key] = max(skip, take)
            else:
                memo[key] = skip
            return memo[key]
        return helper(0)
