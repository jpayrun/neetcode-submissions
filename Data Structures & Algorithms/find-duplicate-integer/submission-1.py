class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memo = {}
        for num in nums:
            memo[num] = 1 + memo.get(num, 0)
        print(memo)
        for num in nums:
            if memo[num] > 1:
                return num