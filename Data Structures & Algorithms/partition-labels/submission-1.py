class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for c in s:
            mp[c] = mp.get(c, 0) + 1
        visited = set()
        res = []
        size = 0
        for c in s:
            visited.add(c)
            size+=1
            if mp[c] == 1:
                visited.remove(c)
            mp[c]-=1
            if not visited:
                res.append(size)
                size=0
        return res