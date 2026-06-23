class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        syms = {'I' : 1, 'V': 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        N = len(s) - 1
        #breakpoint()
        while N >= 0:
            if syms[s[N]] > syms[s[N-1]] and N > 0:
                count+= syms[s[N]] - syms[s[N-1]]
                N-=1
            else:
                count+=syms[s[N]]
            N-=1
        return count    