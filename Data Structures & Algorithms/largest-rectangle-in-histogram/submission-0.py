class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        max_area = 0
        s = []

        for i in range(n + 1):
            while s and (i == n or heights[s[-1]] >= heights[i]):
                height = heights[s.pop()]
                width = i if not s else i - s[-1] - 1
                max_area = max(max_area, height * width)
            s.append(i)
        return max_area