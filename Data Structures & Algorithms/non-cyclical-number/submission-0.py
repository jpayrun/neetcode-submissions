class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        tmp = n
        while True:
            s = 0
            while tmp:
                s += (tmp % 10)**2
                tmp = tmp // 10
            if s == 1:
                return True
            if s in seen:
                return False
            else:
                seen.add(s)
            tmp = s