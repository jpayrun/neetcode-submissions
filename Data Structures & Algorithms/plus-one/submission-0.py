class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] * len(digits)
        carry = 1
        r = len(digits) - 1
        while r >= 0:
            if carry:
                val = digits[r] + 1
                carry = val // 10
                res[r] = val % 10
            else:
                res[r] = digits[r]
            r-=1
        if carry:
            return [1] + [0] * len(digits)
        return res
