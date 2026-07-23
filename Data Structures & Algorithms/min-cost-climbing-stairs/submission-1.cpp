class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> dp (n + 1, INT_MAX);
        return helper(n, dp, cost);
    }

    int helper(int i, vector<int> &dp, vector<vector<int>>::value_type &cost) {
        if (i <= 1) return 0;
        if (dp[i] < INT_MAX) return dp[i];
        dp[i] = min(
            cost[i - 1] + helper(i - 1, dp, cost), 
            cost[i - 2] + helper(i - 2, dp, cost));
        return dp[i];
    }
};
