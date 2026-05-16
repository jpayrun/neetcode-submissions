class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        memo = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            memo[crs].append(pre)
        seen = set()
        def dfs(crs):
            if memo[crs] == []:
                return True
            if crs in seen:
                return False
            seen.add(crs)
            for pre in memo[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            memo[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True