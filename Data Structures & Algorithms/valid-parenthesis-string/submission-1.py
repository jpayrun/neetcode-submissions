class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        r = 0
        for c in s:
            if c == "(":
                l+=1
                r+=1
            elif c == ")":
                l = max(0, l - 1)
                r-= 1
            else:
                l = max(0, l - 1)
                r+=1
            if r < 0:
                return False
        return l == 0