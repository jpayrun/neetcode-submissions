class Solution {
public:
    int integerBreak(int n) {
        unordered_map <int, int> dp;
        dp[1] = 1;
        for (int num = 1; num <= n; num++) {
            dp[num] = num == n ? 0 : num;
            for (int i = 1; i < num; i++) {
                int val = dp[i] * dp[num-i];
                dp[num] = max(dp[num], val);
            }
        }
        return dp[n];
    }
    
};