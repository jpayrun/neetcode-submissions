class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mp = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            mp[crs].append(pre)
        memo = {}
        def dfs(crs, pre):
            if crs == pre:
                return True
            key = (crs, pre)
            if not mp[crs]:
                return False
            if key in memo:
                return memo[key]
            for ncrs in mp[crs]:
                if dfs(ncrs, pre):
                    memo[key] = True
                    return memo[key]
            memo[key] = False
            return memo[key]
        res = []
        for pre, crs in queries:
            res.append(dfs(crs, pre))
        return res