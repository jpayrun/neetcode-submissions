
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)
        self.comp = n
        
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(u, v):
            p1 = find(u)
            p2 = find(v)

            if p1 == p2:
                return False

            self.comp -= 1

            if rank[p1] > rank[p2]:
                p1, p2 = p2, p1
            rank[p1] += rank[p2]
            par[p2] = p1
            return True

        for u, v in edges:
            if not union(u, v):
                return False
        return self.comp == 1

