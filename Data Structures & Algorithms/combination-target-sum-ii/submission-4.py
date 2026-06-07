class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def bt(i, path, current_sum):
            if current_sum == target:
                res.append(path.copy())
                return
            if i == len(candidates) or current_sum > target:
                return
            
            # take
            path.append(candidates[i])
            bt(i+1, path, current_sum + candidates[i])
            # undo
            path.pop()
            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            bt(i+1, path, current_sum)
            return
        bt(0, [], 0)
        return res