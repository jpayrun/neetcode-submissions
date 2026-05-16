class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = set(nums)
        res = 0
        for num in nums:
            if (num - 1) in val:
                continue
            else:
                x = num
                temp = 0
                while x in val:
                    x+=1
                    temp+=1
                res = max(res, temp)
        return res