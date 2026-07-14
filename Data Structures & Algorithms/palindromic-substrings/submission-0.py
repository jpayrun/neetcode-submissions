class Solution:
    def countSubstrings(self, s: str) -> int:
        def pal(s):
            return s == s[::-1]
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if pal(s[i:j]):
                    res+=1
        return res