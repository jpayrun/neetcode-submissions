class Solution {
public:
    vector<int> memo;
    int rob(vector<int>& nums) {
        memo.assign(nums.size(), -1);
        return helper(0, nums);
    }
    int helper(int i, vector<int> &nums) {
        if (i >= nums.size()) return 0;
        if (memo[i] >= 0) return memo[i];
        memo[i] = max(nums[i] + helper(i + 2, nums), helper(i+1, nums));
        return memo[i];
    }
};
