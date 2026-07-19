class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def helper(s):
            if not s:
                return True
            if s in memo:
                return memo[s]
            for word in wordDict:
                if word == s[:len(word)]:
                    memo[s] = helper(s[len(word):])
                    if memo[s]:
                        return memo[s]
            return False
        return helper(s)