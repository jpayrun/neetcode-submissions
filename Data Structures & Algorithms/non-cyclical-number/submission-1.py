class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            res = 0
            while n:
                digit = n % 10
                digit*=digit
                res+=digit
                n = n // 10
            return res
        slow, fast = n, helper(n)
        while slow != fast:
            fast = helper(fast)
            fast = helper(fast)
            slow = helper(slow)
        return fast == 1