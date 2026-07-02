class Solution:
    def simplifyPath(self, path: str) -> str:
        c = 0
        s = []
        while c < len(path):
            if path[c] == "/":
                c += 1
                continue
            
            word = ""
            while c < len(path) and path[c] != "/":
                word += path[c]
                c += 1
            
            if word == "..":
                if s:
                    s.pop()
            elif word == "." or word == "":
                pass
            else:
                s.append(word)
        
        return "/" + "/".join(s)