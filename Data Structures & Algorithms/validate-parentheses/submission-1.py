class Solution:
    def isValid(self, s: str) -> bool:
        left = '({['
        right = {"}" : "{", ")": "(", "]" : "["}
        stack = ''
        for i in s:
            print(stack)
            if i in left:
                stack+=i
            else:
                if not stack:
                    return False
                if right[i] != stack[-1]:
                    return False
                stack = stack[:-1]
        return True if not stack else False

