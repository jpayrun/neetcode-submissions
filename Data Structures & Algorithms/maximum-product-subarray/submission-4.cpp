class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int cur_min = 1, cur_max = 1;
        for (const auto &n : nums) {
            int tmp = cur_max * n;
            cur_max = max(tmp, max(n, cur_min * n));
            cur_min = min(tmp, min(n, cur_min * n));
            res = max(cur_max, res);
        }
        return res;
    }
};
