class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for num in nums:
            if l == 0 or l == 1:
                l+=1
            elif num != nums[l-2]:
                nums[l] = num
                l+=1
        return l