class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for c in s:
            mp[c] = mp.get(c, 0) + 1
        res = []
        i = 0
        visited = set()
        while i < len(s):
            tmp = 0
            visited.add(s[i])
            while visited and i < len(s):
                tmp+=1
                if s[i] not in visited:
                    visited.add(s[i])
                if mp[s[i]] == 1:
                    visited.remove(s[i])
                mp[s[i]]-=1
                i+=1
            res.append(tmp)
        return res
                