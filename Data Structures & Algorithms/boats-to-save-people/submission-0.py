class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l = 0
        r = len(people) - 1
        tot = 0
        while l <= r:
            if (people[l] + people[r]) <= limit: 
                l+=1
                r-=1
            else:
                r-=1
            tot+=1
        return tot