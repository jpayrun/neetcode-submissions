class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur = 0;
        int res = nums[0];
        for (const auto &num : nums){
            cur += num;
            res = max(cur, res);
            if (cur < 0) cur = 0;
        }
        return res;
    }
};
