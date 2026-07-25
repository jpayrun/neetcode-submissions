
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = root.val
        self.c = k
        def dfs(root):
            if not root:
                return
            if self.c == 0:
                return
            dfs(root.left)
            self.c-=1
            if self.c == 0:
                self.res = root.val
            
            dfs(root.right)
        dfs(root)
        return self.res