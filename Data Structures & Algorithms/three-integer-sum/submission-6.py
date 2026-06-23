class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = 0
        while l < len(nums) - 2:
            m = l + 1
            r = len(nums) - 1
            while m < r:
                tmp = [nums[l], nums[m], nums[r]]
                s = sum(tmp)
                if s == 0:
                    res.append(tmp)
                    while m < r and nums[m+1] == nums[m]:
                        m+=1
                    m+=1
                elif s > 0:
                    r-=1
                else:
                    m+=1
            while l < len(nums) - 2 and nums[l+1] == nums[l]:
                l+=1 
            l+=1
        return res