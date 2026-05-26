/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res = root->val;
        dfs(root, &res);
        return res;
    }
    int dfs(TreeNode *root, int *res) {
        if (root == nullptr) return 0;
        int l = dfs(root->left, res);
        int r = dfs(root->right, res);
        l = max(l, 0);
        r = max(r, 0);
        *res = max(*res, l + r + root->val);
        return max(l, r) + root->val;
    }
};
