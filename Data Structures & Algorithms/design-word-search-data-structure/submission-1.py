class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


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
        cur.isEndOfWord = True

    def search_help(self, word, i, cur):
        if i == len(word):
            return cur.isEndOfWord
        if word[i] == '.':
            for child_idx in range(26):
                if cur.children[child_idx]:
                    if self.search_help(word, i + 1, cur.children[child_idx]):
                        return True
            return False
        else:
            idx = ord(word[i]) - ord('a')
            if not cur.children[idx]:
                return False
            return self.search_help(word, i + 1, cur.children[idx])

    
    def search(self, word: str) -> bool:
        cur = self.root
        return self.search_help(word, 0, cur)
