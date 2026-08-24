class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            mp[crs].append(pre)
        seen = set()
        visited = set()
        res = []
        def dfs(crs):

            if crs in seen:
                return False
            if crs in visited:
                return True
            seen.add(crs)
            for ncrs in mp[crs]:
                if not dfs(ncrs):
                    return False
            seen.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []

        return res