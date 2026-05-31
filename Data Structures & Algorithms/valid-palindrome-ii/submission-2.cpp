class Solution {
public:
    bool validPalindrome(string s) {
        return helper(s, 0, s.size() - 1);
    }

    bool helper(string &s, int l, int r, int i = 0) {
        if (l > r) return true;
        if (s[l] == s[r]) return helper(s, l+1, r-1, i);
        if (s[l] != s[r] && i == 1) return false;
        return helper(s, l+1, r, 1) || helper(s, l, r-1, 1);
    }
};