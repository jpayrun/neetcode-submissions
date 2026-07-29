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
    unordered_map <TreeNode*, int> memo;
    int rob(TreeNode* root) {
        return dfs(root);
    }
    int dfs(TreeNode *root) {
        if (memo.count(root) == 1) return memo[root];
        if (!root) return 0;
        memo[root] = root->val;
        if (root->left != nullptr) {
            memo[root] += dfs(root->left->left) + dfs(root->left->right);
        }
        if (root->right) {
            memo[root] += dfs(root->right->left) + dfs(root->right->right);
        }
        memo[root] = max(memo[root], dfs(root->left) + dfs(root->right));
        return memo[root];
    }
};