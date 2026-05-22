class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        self.res = n

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return
            self.res -=1
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            rank[p1] += rank[p2]
            par[p2] = p1

        for n1, n2 in edges:
            union(n1, n2)

        return self.res