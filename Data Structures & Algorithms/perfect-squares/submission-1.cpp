class Solution {
public:
    vector<vector<int>> memo;
    int numSquares(int n) {
        memo.resize(n + 1, vector<int>(n+1, -1));
        return helper(2, n);
    }
    int helper(int i, int n) {
        if (i * i > n) return n;
        if (n <= 3) return n;
        if (memo[i][n] >= 0) return memo[i][n];
        int take = 1 + helper(i, n - i * i);
        int skip = helper(i+1, n);
        memo[i][n] = min(take, skip);
        return memo[i][n];
    }
};