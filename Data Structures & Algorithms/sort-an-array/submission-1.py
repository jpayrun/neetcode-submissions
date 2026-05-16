import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) <= 1:
                return nums
            low = []
            high = []
            # pivot = nums.pop()
            pivot = random.choice(nums)
            mid = []
            for num in nums:
                if num < pivot:
                    low.append(num)
                elif pivot == num:
                    mid.append(num)
                else:
                    high.append(num)
            return quicksort(low) + mid + quicksort(high)
        return quicksort(nums)