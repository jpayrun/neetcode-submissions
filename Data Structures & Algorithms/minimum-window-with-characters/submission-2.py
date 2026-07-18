class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_mp = {}
        t_mp = {}
        for c in s:
            s_mp[c] = s_mp.get(c, 0) + 1
        for c in t:
            t_mp[c] = t_mp.get(c, 0) + 1
        def check(mp_s, mp_t):
            for key in mp_t:
                if key in mp_s and mp_s[key] >= mp_t[key]:
                    continue
                else:
                    return False
            return True
        l = 0
        res = s
        if not check(s_mp, t_mp):
            return ''
        temp = {}
        temp_s = ''
        for r in range(len(s)):
            temp[s[r]] = temp.get(s[r], 0) + 1
            temp_s += s[r]
            while check(temp, t_mp):
                if len(res) > len(temp_s):
                    res = temp_s
                temp[s[l]]-=1
                l+=1
                temp_s = temp_s[1:]

        return res