class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # memo = {}
        self.res = []
        def helper(s, path):
            key = (s, path)
            if not s:
                tmp = ' '.join(path)
                self.res.append(tmp)
                return
            # if key in memo:
            #     return memo[key]
            for word in wordDict:
                if word == s[:len(word)]:
                    path.append(word)
                    helper(s[len(word):], path)
                    path.pop()
            return
        helper(s, [])
        return self.res