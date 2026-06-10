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
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        return dfs(root1, root2, target);
    }
    bool dfs(TreeNode *root1, TreeNode *root2, int target) {
        if (root1 == nullptr || root2 == nullptr) return false;
        if (root1->val + root2->val == target) return true;
        if (root1->val + root2->val > target) {
            return dfs(root1->left, root2, target) || dfs(root1, root2->left, target);
        } else {
            return dfs(root1->right, root2, target) || dfs(root1, root2->right, target);
        }
    }
};
