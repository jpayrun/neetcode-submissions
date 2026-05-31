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
    int res = 0;
    int goodNodes(TreeNode* root) {
        dfs(root, root->val);
        return res;
    }
    void dfs(TreeNode *root, int top) {
        if (root == nullptr) return;
        if (root->val >= top) {
            top = max(top, root->val);
            res++;
        }
        dfs(root->left, top);
        dfs(root->right, top);
    }
};
