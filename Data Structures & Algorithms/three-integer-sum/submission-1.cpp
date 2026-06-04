class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int l = 0;
        int n = nums.size() - 1;
        int r = n;
        int m;
        vector<vector<int>> res;
        while (l < n) {
            r = n;
            m=l+1;
            while (m < r) {
                int tot = nums[l] + nums[r] + nums[m];
                if (tot == 0) {
                    res.push_back({nums[l], nums[r], nums[m]});
                    while (r > m && nums[r] == nums[r-1]) r--;
                    r--;
                }
                else if (tot < 0) m++;
                else r--;
            }
            while (nums[l] == nums[l+1] and l < n - 1) {
                l++;
            }
            l++;
        }
        return res;
    }
};
