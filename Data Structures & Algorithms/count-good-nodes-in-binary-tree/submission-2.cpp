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
    int goodNodes(TreeNode* root) {
        return dfs(root, INT_MIN);
        
    }
    int dfs(TreeNode *root, int top) {
        if (root == nullptr) return 0;
        int res = root->val >= top ? 1 : 0;
        top = max(root->val, top);
        res+= dfs(root->left, top);
        res+= dfs(root->right, top);
        return res;
    }
};
