class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> path;
        bt(0, target, nums, path);
        return res;
    }
    void bt(int i, int target, vector<int> &nums, vector<int> &path, int tot = 0) {
        if (i == nums.size() && target == tot) {
            res.push_back(path);
            return;
        }
        if (i == nums.size()) return;
        if (tot > target) return;
        path.push_back(nums[i]);
        bt(i, target, nums, path, tot+nums[i]);
        path.pop_back();
        bt(i+1, target, nums, path, tot);
    }
};
