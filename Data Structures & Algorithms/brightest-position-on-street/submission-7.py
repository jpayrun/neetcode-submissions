class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        diff = defaultdict(int)

        for pos, rng in lights:
            start, end = pos - rng, pos + rng

            diff[start] += 1
            diff[end + 1] -= 1

        max_bright = -float('inf')
        cur = 0
        res = 0

        for key in sorted(diff):
            cur += diff[key]
            if cur > max_bright:
                max_bright = cur
                res = key
        return res
            