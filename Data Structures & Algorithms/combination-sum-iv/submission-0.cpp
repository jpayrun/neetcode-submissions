class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> memo(target+1, 0);
        memo[target] = 1;
        sort(nums.begin(), nums.end());
        for (int i = target - 1; i >= 0; i--) {
            for (const auto num : nums) {
                if (i + num <= target) {
                    memo[i] += memo[i+num];
                }
            }
        }
        return memo[0];
    }
};