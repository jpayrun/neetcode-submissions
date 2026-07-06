class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_mp = {}
        t_mp = {}
        for c in s:
            s_mp[c] = s_mp.get(c, 0) + 1
        for c in t:
            t_mp[c] = t_mp.get(c, 0) + 1
        def check(x):
            for key in t_mp.keys():
                if key not in x or x[key] < t_mp[key]:
                    return False
            return True
        if not check(s_mp):
            return ""
        l = 0
        r = len(s) - 1
        res = s
        temp = {}
        temp_str = ""
        for r in range(len(s)):
            temp[s[r]] = temp.get(s[r], 0) + 1
            temp_str+=s[r]
            while check(temp):
                if len(temp_str) < len(res):
                    res = temp_str
                temp[s[l]]-=1
                l+=1
                temp_str = temp_str[1:]
        return res