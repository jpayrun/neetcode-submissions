class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int cur_sum = 0;
        for (int num : nums) {
            cur_sum = Math.max(cur_sum + num, num);
            res = Math.max(cur_sum, res);
        }
        return res;
    }
}
