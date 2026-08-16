# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2
        l = self.mergeSort(pairs[:m])
        r = self.mergeSort(pairs[m:])
        return self.sort(l, r)
        
    def sort(self, l, r):
        L = len(l)
        R = len(r)
        k = 0
        i = 0
        j = 0
        arr = [0] * (L + R)
        while i < L and j < R:
            if l[i].key <= r[j].key:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        while i < L:
            arr[k] = l[i]
            i+=1
            k+=1
        while j < R:
            arr[k] = r[j]
            j+=1
            k+=1
        return arr
