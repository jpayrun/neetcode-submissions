class Solution:
    def maxSatisfied(self, cust: List[int], grumpy: List[int], minutes: int) -> int:
        tot = 0
        l = [0] * len(grumpy)
        cur_l = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                tot+=cust[i]
            if grumpy[i] == 1:
                cur_l+=cust[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                cur_l-=cust[i - minutes]
            l[i] = cur_l
        return tot + max(l)