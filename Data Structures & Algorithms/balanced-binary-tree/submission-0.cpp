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
    bool result = true;
    bool isBalanced(TreeNode* root) {
        dfs(root);
        return result;
    }
    int dfs(TreeNode *root) {
        if (root == nullptr) return 0;

        int l = dfs(root->left) + 1;
        int r = dfs(root->right) + 1;

        if (abs(l - r) > 1) {
            result = false;
        }
        return max(l, r);
    }
};
