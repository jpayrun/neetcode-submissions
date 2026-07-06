class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> memo (nums.size(), 1);
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) memo[i] = max(memo[j] + 1, memo[i]);
            }
        }
        int res = 1;
        for (int i = 0; i < nums.size(); i++) {
            res = max(memo[i], res);
        }
        return res;
    }
};
