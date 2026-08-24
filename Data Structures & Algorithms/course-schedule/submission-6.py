class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {}
        for i in range(numCourses):
            mp[i] = []
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        seen = set()
        def dfs(crs):
            if mp[crs] == []:
                return True
            if crs in seen:
                return False
            seen.add(crs)
            for ncrs in mp[crs]:
                if not dfs(ncrs):
                    return False
            seen.remove(crs)
            mp[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True