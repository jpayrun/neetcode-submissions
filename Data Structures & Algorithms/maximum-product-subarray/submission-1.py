class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1
        for num in nums:
            temp = cur_max * num
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(num * cur_min, temp, num)
            res = max(cur_max, res)
        return res
            