class Solution:
    def countElements(self, arr: List[int]) -> int:
        mp = set(arr)
        # visited = set()
        res = 0
        for num in arr:
            if num+1 in mp:
                res+=1
        return res
