# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        def dfs(root, i=0):
            if not root:
                return
            res[i] = res.get(i, []) + [root.val]
            dfs(root.left, i+1)
            dfs(root.right, i+1)
        dfs(root)
        return list(res.values())