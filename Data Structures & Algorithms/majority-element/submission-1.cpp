class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> vals;
        for (const auto &num : nums) {
            if (vals.count(num) == 0) vals[num] = 1;
            else vals[num]++;
        }
        int m_key = 0;
        int res;
        for (const auto &[key, val] : vals) {
            if (vals[key] > m_key) {
                res = key;
                m_key = vals[key];
            }
        }
        return res;
    }
};