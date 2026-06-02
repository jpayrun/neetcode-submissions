class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pre;
        vector<int> post(nums.size());
        int tot = 1;
        for (const auto &num : nums) {
            tot *= num;
            pre.push_back(tot);
        }
        tot = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            tot *= nums[i];
            post[i] = tot;
        }
        vector<int> res(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) res[i] = post[i+1];
            else if (i == nums.size() - 1) res[i] = pre[i-1];
            else res[i] = pre[i-1] * post[i+1];
        }
        return res;
    }
};
