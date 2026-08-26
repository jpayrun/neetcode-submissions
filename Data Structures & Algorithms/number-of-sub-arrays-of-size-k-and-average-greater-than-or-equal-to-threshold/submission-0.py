class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        r = 0
        tot = 0
        while r < len(arr):
            tot+=arr[r]
            r+=1
            if r - l > k:
                tot-=arr[l]
                l+=1
            if r - l == k:
                if tot / k >= threshold:
                    res+=1
        return res
