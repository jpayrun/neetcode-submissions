class Solution {
public:
    int res = INT_MAX;
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        int tot = 0;
        for (int r = 0; r < nums.size(); r++) {
            tot+=nums[r];
            while (r - l + 1 > res) {
                tot-=nums[l];
                l++;
            }
            while (tot >= target) {
                res = min(r - l + 1, res);
                if (res == 1) return res;
                tot-=nums[l];
                l++;
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};