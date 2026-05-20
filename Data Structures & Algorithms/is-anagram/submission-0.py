class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        s_dict = {}
        for i in s:
            s_dict[i] = 1 + s_dict.get(i, 0)
        t_dict = {}
        for i in t:
            t_dict[i] = 1 + t_dict.get(i, 0)
        for i in s_dict:
            if s_dict[i] != t_dict[i]:
                return False
        return True