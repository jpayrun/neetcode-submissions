class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = [dict() for _ in strs]
        for i, ss in enumerate(strs):
            for s in ss:
                dict_list[i][s] = 1 + dict_list[i].get(s, 0)
        
        res = []
        seen = set()
        for i in range(len(dict_list)):
            if i in seen:
                continue
            temp = [strs[i]]
            seen.add(i)
            for j in range(i+1, len(dict_list)):
                if j in seen:
                    continue
                if dict_list[i] == dict_list[j]:
                    temp.append(strs[j])
                    seen.add(j)
            res.append(temp)
        return res