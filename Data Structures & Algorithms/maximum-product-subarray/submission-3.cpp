class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int cur_min = 1, cur_max = 1;
        for (const int n : nums) {
            int tmp = cur_max * n;
            cur_max = max(max(tmp, n), cur_min * n);
            cur_min = min(min(tmp, n), cur_min * n);
            res = max(res, cur_max);
        }
        return res;
    }
};
