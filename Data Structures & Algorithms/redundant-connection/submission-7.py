class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = [0] * n
        for i in range(n):
            par[i] = i
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        def union(e1, e2):
            p1, p2 = find(e1), find(e2)
            if p1 == p2:
                return True
            par[p1] = p2
        for e1, e2 in edges:
            if union(e1, e2):
                return [e1, e2]
        return []