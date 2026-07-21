class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c:i for i, c in enumerate(order)}

        def comp(word):
            return [order_index[c] for c in word]
        
        return words == sorted(words, key=comp)