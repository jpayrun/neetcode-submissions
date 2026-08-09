class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque()
        for s in students:
            q.append(s)
        i = 0
        eat = 1
        while q:
            if eat == 0:
                break
            eat = 0
            for _ in range(len(q)):
                want = q.popleft()
                if want == sandwiches[i]:
                    i+=1
                    eat = 1
                else:
                    q.append(want)
        return len(sandwiches) - i