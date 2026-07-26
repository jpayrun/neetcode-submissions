class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for c in num1:
            n1*=10
            n1+=int(c)
        for c in num2:
            n2*=10
            n2+=int(c)
        tmp = n1 * n2
        res = ''
        while tmp > 0:
            res = str(tmp%10) + res
            tmp//=10
        return "0" if not res else res
        