class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map <char, int> a;
        int l = 0;
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (a.count(s[i]) == 1) {
                l = max(l, a[s[i]]+1);
            }
            a[s[i]]=i;
            res = max(res, i - l + 1);
        }
        return res;
    }
};
