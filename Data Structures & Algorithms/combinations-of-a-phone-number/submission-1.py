class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.res = []
        if not digits:
            return self.res
        def bt(i, s, path):
            if i == len(s):
                self.res.append(path)
                return
            for c in l[s[i]]:
                path+=c
                bt(i+1, s, path)
                path=path[:-1]
        bt(0, digits, '')
        return self.res
