class Solution:
    def maxSatisfied(self, cust: List[int], grumpy: List[int], minutes: int) -> int:
        tot = 0
        l = [0] * len(cust)
        g = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                tot+=cust[i]
            if grumpy[i] == 1:
                g+=cust[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                g-=cust[i - minutes]
            l[i] = g
        return tot + max(l)