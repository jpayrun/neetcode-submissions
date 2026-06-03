class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        vector<int> memo(s.size()+1, -1);
        return helper(0, s, memo, n);
    }
    int helper(int i, string &s, vector<int> &memo, int n) {
        if (i == n) return 1;
        if (s[i] == '0') return 0;
        if (memo[i] >= 0) return memo[i];
        int res = 0;
        // Add 
        if ((i + 1) < n && s[i] == '1' || ((i+1) < n && s[i] == '2' && s[i+1] <= '6')) {
            res = helper(i+2, s, memo, n) + helper(i+1, s, memo, n);
        } else {
            res = helper(i+1, s, memo, n);
        }
        memo[i] = res;
        return memo[i];
    }
};
