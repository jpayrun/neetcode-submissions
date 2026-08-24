# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        def dfs(root, path = []):
            path.append(root.val)
            if not root.left and not root.right:
                paths.append(path.copy())
                return
            if root.left:
                dfs(root.left, path)
                path.pop()
            if root.right:
                dfs(root.right, path)
                path.pop()
        dfs(root)
        res = 0
        for path in paths:
            tmp = 0
            for n in path:
                tmp*=10
                tmp+=n
            print(tmp)
            res+=tmp
        return res