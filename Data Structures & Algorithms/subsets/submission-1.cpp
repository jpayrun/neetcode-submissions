class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> subsets(vector<int>& nums) {
        res.push_back(vector<int>());
        bt(0, nums);
        return res;
    }
    void bt(int s, vector<int> &nums) {
        if (s == nums.size()) return;
        vector<vector<int>> temp = res;
        for (const auto &vec : temp) {
            vector<int> add = vec;
            add.push_back(nums[s]);
            res.push_back(add);
        }
        bt(s+1, nums);
    }
};
