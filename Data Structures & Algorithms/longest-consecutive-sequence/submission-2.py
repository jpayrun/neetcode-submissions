class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if num - 1 in s:
                continue
            i = 0
            while num + i in s:
                i+=1
                res = max(res, i)
        return res