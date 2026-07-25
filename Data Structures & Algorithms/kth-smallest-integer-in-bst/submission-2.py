
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            s.append(root.val)
            dfs(root.right)
            
        dfs(root)
        return s[k-1]