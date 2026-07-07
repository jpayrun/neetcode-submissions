class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        for (const auto num : nums) {
            s.insert(num);
        }
        int res = 0;
        for (const auto num : nums) {
            if (s.count(num-1)) continue;
            int tmp = 0;
            while (s.count(num + tmp)) {
                res = max(res, ++tmp);
            }
        }
        return res;
    }
};
