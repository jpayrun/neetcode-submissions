class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for op in operations:
            if "0" <= op <= "9" or op[0] == "-":
                s.append(int(op))
            elif op == "+":
                s.append(s[-2] + s[-1])
            elif op == "C":
                s.pop()
            else:
                s.append(s[-1] * 2)
        return sum(s)