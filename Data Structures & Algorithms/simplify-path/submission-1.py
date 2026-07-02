class Solution:
    def simplifyPath(self, path: str) -> str:
        c = 0
        s = []

        while c < len(path):
            if path[c] == "/":
                c+=1
            
            word = ""
            while c < len(path) and path[c] != "/":
                word+=path[c]
                c+=1
            
            if word == "." or word == "":
                continue
            if word == ".." and s:
                s.pop()
            elif word == "..":
                continue
            else:
                s.append(word)
        return "/" + "/".join(s)