# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l == -1:
                root.left = None

            if r == -1:
                root.right = None

            if max(l, r) <= 0 and root.val == target:
                return -1
            return root.val
        res = dfs(root)
        return None if res <= 0 else root