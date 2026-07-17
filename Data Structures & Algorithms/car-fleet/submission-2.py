class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = [(s, p) for s, p in zip(position, speed)]
        mp.sort(key=lambda x: -x[0])
        res = []
        for p, s in mp:
            res.append((target - p) / s)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)