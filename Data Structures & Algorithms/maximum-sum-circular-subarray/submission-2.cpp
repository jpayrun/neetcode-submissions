class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int cur_max = 0, cur_min = 0, glob_max = nums[0], glob_min = nums[0], total = 0;
        for (int n : nums) {
            cur_max = max(cur_max + n, n);
            cur_min = min(cur_min + n, n);
            total+=n;
            glob_max = max(glob_max, cur_max);
            glob_min = min(glob_min, cur_min);
        }

        return glob_max < 0 ? glob_max : max(glob_max, total - glob_min);
    }
};