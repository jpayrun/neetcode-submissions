class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        q = deque([("0000", 0)])
        visited = set(deadends)
        visited.add("0000")
        def children(lock):
            res = []
            for i in range(4):
                digit1 = str((int(lock[i]) + 1 ) % 10)
                res.append(lock[:i] + digit1 + lock[i+1:])
                digit2 = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit2 + lock[i+1:])
            return res
        
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns + 1))
        return -1