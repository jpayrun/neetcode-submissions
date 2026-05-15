class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}
        for i, num in enumerate(nums):
            if num in memo:
                if abs(memo[num] - i) <= k:
                    return True
            memo[num] = i
        return False