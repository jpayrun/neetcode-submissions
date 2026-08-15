class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)
        return max(memo)
