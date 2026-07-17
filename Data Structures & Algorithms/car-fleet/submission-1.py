class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = []
        for p, s in zip(position, speed):
            mp.append((p, s))
        mp.sort(key=lambda x: -x[0])
        res = []
        def time(x):
            return (target - x[0]) / x[1]
        for i in range(len(mp)):
            res.append(time(mp[i]))
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        return len(res)