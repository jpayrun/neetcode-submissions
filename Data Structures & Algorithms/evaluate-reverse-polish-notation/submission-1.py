class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        res = 0
        for c in tokens:
            if c == '+':
                b, a = int(s.pop()), int(s.pop())
                s.append(a + b)
            elif c == '-':
                b, a = int(s.pop()), int(s.pop())
                s.append(a - b)
            elif c == "/":
                b, a = int(s.pop()), int(s.pop())
                s.append(int(a / b))
            elif c == "*":
                b, a = int(s.pop()), int(s.pop())
                s.append(a * b)
            else:
                s.append(c)
        return int(s[0])