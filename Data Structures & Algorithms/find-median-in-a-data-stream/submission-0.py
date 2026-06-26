class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        self.nums.sort()
        if n % 2 == 0:
            r = n // 2
            l = r - 1
            return (self.nums[l] + self.nums[r]) / 2
        m = n // 2
        return self.nums[m]
        