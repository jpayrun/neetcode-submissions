class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}
        res = 0
        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        for key, val in mp.items():
            if val == 1:
                res = key
        return res
