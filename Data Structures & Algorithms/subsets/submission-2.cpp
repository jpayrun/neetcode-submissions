class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> subsets(vector<int>& nums) {
        res.push_back(vector<int>());
        bt(0, nums);
        return res;
    }
    void bt(int i, vector<int> &nums) {
        if (i == nums.size()) return;
        vector<vector<int>> vals = res;
        for (const auto &vec : vals) {
            vector<int> temp = vec;
            temp.push_back(nums[i]);
            res.push_back(temp);
        }
        bt(i+1, nums);
    }
};
