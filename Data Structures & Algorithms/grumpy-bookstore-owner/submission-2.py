class Solution:
    def maxSatisfied(self, cust: List[int], grumpy: List[int], minutes: int) -> int:
        tot = 0
        grump = [0] * (len(cust))
        cur_grump = 0
        for i in range(len(cust)):
            if grumpy[i] == 0:
                tot+=cust[i]
            if grumpy[i] == 1:
                cur_grump+=cust[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                cur_grump-=cust[i - minutes]
            if i >= minutes - 1:
                grump[i] = cur_grump
        print(grump)
        return tot + max(grump)