class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            if len(s1) > len(s2):
                return False
                # s1, s2 = s2, s1
            return s1 == s2[:len(s1)] and s1 == s2[-len(s1):]
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res+=1
        return res