class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n
        r_l_min = [0] * n
        for i in range(1, n):
            l_max[i] = max(l_max[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            r_max[i] = max(r_max[i+1], height[i+1])
        for i in range(n):
            r_l_min[i] = min(l_max[i], r_max[i])
        res = 0
        for i in range(n):
            res+=max(r_l_min[i] - height[i], 0)
        return res