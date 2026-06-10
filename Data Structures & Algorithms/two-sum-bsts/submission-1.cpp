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
    void dfs(TreeNode* currNode, unordered_set<int>& nodeSet) {
        if (currNode == nullptr) {
            return;
        }
        dfs(currNode->left, nodeSet);
        nodeSet.insert(currNode->val);
        dfs(currNode->right, nodeSet);
    }

    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        unordered_set<int> nodeSet1, nodeSet2;
        dfs(root1, nodeSet1);
        dfs(root2, nodeSet2);

        for (int value1 : nodeSet1) {
            if (nodeSet2.count(target - value1)) {
                return true;
            }
        }

        return false;
    }
};
