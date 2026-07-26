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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        return dfs(root, subRoot);
    }
    bool sameTree(TreeNode *t1, TreeNode *t2) {
        if (t1 == nullptr && t2 == nullptr) return true;
        if (t1 == nullptr || t2 == nullptr) return false;
        if (t1->val != t2->val) return false;
        return sameTree(t1->left, t2->left) && sameTree(t1->right, t2->right);
    }
    bool dfs(TreeNode *root, TreeNode *subRoot) {
        if (root == nullptr) return false;
        if (root->val == subRoot->val) {
            if (sameTree(root, subRoot)) return true;
        }
        bool l = dfs(root->left, subRoot);
        bool r = dfs(root->right, subRoot);
        return l || r;
    }
};
