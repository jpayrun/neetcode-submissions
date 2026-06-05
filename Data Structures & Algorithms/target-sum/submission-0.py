class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        res = 0
        def helper(i, tot = 0):
            key = (i, tot)
            if i == len(nums) and tot == target:
                return 1
            if i == len(nums):
                return 0
            if key in memo:
                return memo[key]
            memo[key] = helper(i+1, tot+nums[i]) + helper(i+1, tot-nums[i])
            return memo[key]
        return helper(0,0)
            