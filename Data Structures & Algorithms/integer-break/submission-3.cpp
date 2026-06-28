class Solution {
public:
    int integerBreak(int n) {
        unordered_map <int, int> dp;
        dp[1] = 1;
        return helper(n, dp, n);
    }
    int helper(int n, unordered_map<int, int> &dp, int num) {
        if (dp.count(n) == 1 && n != num) return dp[n];
        int res = n == num ? 0 : n;
        for (int i = 1; i < n; i++) {
            int val = helper(i, dp, num) * helper(n - i, dp, num);
            res = max(val, res);
        }
        dp[n] = res;
        return dp[n];
    }
};