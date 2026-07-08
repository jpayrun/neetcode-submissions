
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
            
        dfs(root)
        return self.res[k-1]