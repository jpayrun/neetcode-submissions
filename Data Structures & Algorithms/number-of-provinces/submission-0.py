class Solution:
    def findCircleNum(self, con: List[List[int]]) -> int:
        n = len(con)
        vis = [0] * n
        res = 0
        def dfs(x):
            vis[x] = 1
            for i in range(n):
                if con[x][i] == 1 and vis[i] == 0:
                    dfs(i)
        for i in range(n):
            if vis[i] == 0:
                res+=1
                dfs(i)
        return res