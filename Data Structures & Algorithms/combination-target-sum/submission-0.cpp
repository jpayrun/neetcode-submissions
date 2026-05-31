class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> path;
        backtrack(0, path, nums, target);
        return res;
    }
    void backtrack(int i, vector<int> &path, vector<int> &nums, int target) {
        // accumulate(path.begin(), path.end())
        int total = accumulate(path.begin(), path.end(), 0);
        if (total > target) return;
        if (i == nums.size() && total == target) {
            res.push_back(path);
        }
        if (i == nums.size()) return;
        path.push_back(nums[i]);
        backtrack(i, path, nums, target);
        path.pop_back();
        backtrack(i+1, path, nums, target);
        return;
    }
};
