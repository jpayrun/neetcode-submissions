# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(p, q):
            if not p or not q:
                return False
            if p.val + q.val == target:
                return True
            if p.val + q.val > target:
                return dfs(p.left, q) or dfs(p, q.left)
            else:
                return dfs(p.right, q) or dfs(p, q.right)
        return dfs(root1, root2)