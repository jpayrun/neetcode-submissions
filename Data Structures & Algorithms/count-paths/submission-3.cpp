class Solution {
public:
    vector<vector<int>> memo;
    int uniquePaths(int m, int n) {
        memo.resize(m, vector<int>(n, 0));
        return helper(m-1, n-1);
    }
    int helper(int i, int j) {
        if (i == 0 && j == 0) return 1;
        if (i < 0 || j < 0) return 0;
        if (memo[i][j] > 0) return memo[i][j];
        memo[i][j] = helper(i-1, j) + helper(i, j-1);
        return memo[i][j];
    }
};
