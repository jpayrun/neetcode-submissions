class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0;
        int temp = 0;
        for (const auto &num : nums) {
            if (num == 1) {
                temp++;
            } else {
                res = max(res, temp);
                temp = 0;
            }
        }
        res = max(res, temp);
        return res;
    }
};