class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff(w1, w2):
            return abs(len(set(w1)) - len(set(w2)))
        def comp(w1, w2):
            res = len(w1)
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    res-=1
            return res
        dist = {}
        heap = []
        heapq.heappush(heap, (1, 0, beginWord))
        while heap:
            time, _, word = heapq.heappop(heap)
            print(f"{word} {time}")
            if word == endWord:
                return time
            if word in dist and dist[word] < time:
                continue
            dist[word] = time
            for w in wordList:
                if comp(w, word) <= 1:
                    heapq.heappush(heap, (time +1, diff(w, word), w))
        return 0