class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [0] * (n + 1)
        for i in range(n + 1):
            par[i] = i
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        for e1, e2 in edges:
            p1, p2 = find(e1), find(e2)
            if p1 == p2:
                return [e1, e2]
            par[p1] = p2
        return []