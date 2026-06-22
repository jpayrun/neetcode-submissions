class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur = 0;
        int res = nums[0];
        for (const auto &num : nums){
            cur = max(num, cur+num);
            res = max(cur, res);
        }
        return res;
    }
};
