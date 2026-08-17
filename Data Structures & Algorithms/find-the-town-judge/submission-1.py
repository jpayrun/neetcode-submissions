class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incom = defaultdict(int)
        outcom = defaultdict(int)

        for pers, trus in trust:
            outcom[pers]+=1
            incom[trus]+=1
        
        for key, val in incom.items():
            if val == n - 1:
                if outcom[key] == 0:
                    return key
        return -1