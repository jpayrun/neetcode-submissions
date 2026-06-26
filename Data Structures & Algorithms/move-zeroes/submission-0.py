class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        num = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[l] = nums[l], nums[i]
                num+=1
                l+=1
        for i in range(len(nums)):
            if num > 0:
                num-=1
            else:
                nums[i] = 0
        