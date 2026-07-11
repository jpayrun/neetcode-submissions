class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    tot = nums[i] + nums[j] + nums[l] + nums[r]
                    if target == tot:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l + 1 < r and nums[l] == nums[l+1]:
                            l+=1
                        while l < r -1 and nums[r] == nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif tot < target:
                        l+=1
                    else:
                        r-=1
        return res
