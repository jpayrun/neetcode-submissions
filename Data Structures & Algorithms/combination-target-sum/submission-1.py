class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i, path):
            if i == len(nums) and sum(path) == target:
                res.append(path.copy())
            if i == len(nums):
                return
            if sum(path) > target:
                return
            path.append(nums[i])
            bt(i, path)
            path.pop()
            bt(i+1, path)
        bt(0, [])
        return res