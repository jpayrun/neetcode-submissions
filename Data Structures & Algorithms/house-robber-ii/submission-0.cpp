class Solution {
public:
    vector<int> memo;
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        memo.assign(nums.size(), -1);
        int case1 = helper(0, nums.size() - 2, nums);
        memo.assign(nums.size(), -1);
        int case2 = helper(1, nums.size() - 1, nums);
        return max(case1, case2);
    }
    int helper(int i, int end, vector<int> &nums) {
        if (i > end) return 0;
        if (memo[i] > -1) return memo[i];
        memo[i] = max(nums[i] + helper(i+2, end, nums), helper(i+1, end, nums));
        return memo[i];
    }
};
