class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0;
        int cnt = 0;
        for (const auto &num : nums) {
            cnt = num ? cnt + 1 : 0;
            res = max(res, cnt);
        }
        return res;
    }
};