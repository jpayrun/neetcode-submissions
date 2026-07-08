# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, m = -float('inf')):
            if not root:
                return
            if root.val >= m:
                m = root.val
                self.res+=1
            dfs(root.left, m)
            dfs(root.right, m)
        dfs(root)
        return self.res