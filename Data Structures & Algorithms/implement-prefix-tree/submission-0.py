class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.end_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return cur.end_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return True

        