class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while s[r] == " ":
            s = s[:-1]
            r-=1
        spilt = s.split(" ")
        return len(spilt[-1])