class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in memo:
                return [memo[comp], i]
            memo[num] = i
