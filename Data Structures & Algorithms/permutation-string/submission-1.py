class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1) - 1
        s1_dict = {}
        for s in s1:
            s1_dict[s] = 1 + s1_dict.get(s, 0)
        while r < len(s2):
            if set(s1) != set(s2[l:r+1]):
                r+=1
                l+=1
            s2_dict = {}
            for s in s2[l:r+1]:
                s2_dict[s] = 1 + s2_dict.get(s, 0)
            if s1_dict == s2_dict:
                return True
            l+=1
            r+=1
        return False
            
