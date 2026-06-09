class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pre;
        vector<int> pos(nums.size());
        vector<int> res;
        int tot = 1;
        for (const auto num : nums) {
            tot*=num;
            pre.push_back(tot);
        }
        tot = 1;
        for (int i = 0; i < nums.size(); i++) {
            tot*=nums[nums.size() - i - 1];
            pos[nums.size() - i - 1] = tot;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (i == 0) res.push_back(pos[1]);
            else if (i == nums.size() - 1) res.push_back(pre[i - 1]);
            else res.push_back(pre[i-1] * pos[i+1]);
        }
        return res;
    }
};
