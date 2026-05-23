class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for val in strs:
            count = [0] * 26
            for s in val:
                count[ord(s) - ord('a')] += 1
            res[tuple(count)].append(val)
        return list(res.values())