class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        ss = self.subsets(nums[1:])
        res = ss.copy()

        for s in ss:
            s_copy = s.copy()
            s_copy.append(nums[0])
            res.append(s_copy)
        return res
    