class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = t = 0
        mp = {}
        while r < len(s):
            mp[s[r]] = mp.get(s[r], 0) + 1
            while (r - l + 1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            t = max(t, r - l + 1)
            r += 1
        return t