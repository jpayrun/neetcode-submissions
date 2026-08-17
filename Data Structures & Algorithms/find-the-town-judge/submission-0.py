class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incom = {i : 0 for i in range(1, n + 1)}
        outcom = {i : 0 for i in range(1, n + 1)}
        
        for tust, pers in trust:
            incom[pers]+=1
            outcom[tust]+=1

        
        for key, val in incom.items():
            if val == n - 1:
                if outcom[key] == 0:
                    return key
        return -1