class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(j, cur):
            if j == len(word):
                return cur.end
            if word[j] == ".":
                for i in range(26):
                    if cur.children[i]:
                        if dfs(j + 1, cur.children[i]):
                            return True
                return False
            i = ord(word[j]) - ord('a')
            if not cur.children[i]:
                return False
            return dfs(j + 1, cur.children[i])
        return dfs(0, self.root)
