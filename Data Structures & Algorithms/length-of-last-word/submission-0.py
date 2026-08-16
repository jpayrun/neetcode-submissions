class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        spilt = s.split(" ")
        return len(spilt[-1])