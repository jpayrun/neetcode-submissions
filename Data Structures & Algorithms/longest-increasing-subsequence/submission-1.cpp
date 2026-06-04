class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> memo(nums.size(), 1);
        for (int i = nums.size() - 1; i >= 0; i--) {
            for (int j = i; j < nums.size(); j++) {
                if (nums[i] < nums[j]) memo[i] = max(memo[i], 1 + memo[j]);
            }
        }
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            res = max(res, memo[i]);
        }
        return res;
    }
};
