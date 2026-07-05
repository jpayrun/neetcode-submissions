class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0;
        unordered_map<char, int> mp;
        int res = 0;
        int mf = 0;
        for (int r = 0; r < s.size(); r++) {
            mp[s[r]]++;
            mf = max(mf, mp[s[r]]);
            while (r - l + 1 + - mf > k) {
                mp[s[l]]--;
                l++;
            }
            res = max(res, r - l + 1);
        } 
        return res;
    }
};
