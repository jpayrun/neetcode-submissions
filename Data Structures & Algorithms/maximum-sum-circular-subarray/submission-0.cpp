class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int cur_max = 0, global_max = nums[0], cur_min = 0, global_min = nums[0], total = 0;
        for (int num : nums) {
            total+=num;
            cur_max = max(cur_max + num , num);
            // cur_max = max(cur_max, num);
            global_max = max(cur_max, global_max);
            // cur_min = min(cur_min, num);
            cur_min = min(cur_min + num, num);
            global_min = min(cur_min, global_min);
        }
        if (global_max < 0) return global_max;
        global_max = max(global_max, total - global_min);
        return global_max;
    }
};