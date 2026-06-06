class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set <char> a;
        int l = 0;
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            while (a.count(s[i]) == 1) {
                a.erase(s[l]);
                l++;
            }
            a.insert(s[i]);
            res = max(res, i - l + 1);
        }
        return res;
    }
};
