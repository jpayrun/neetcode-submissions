class Solution {
public:
    vector<vector<int>> memo;
    int uniquePaths(int m, int n) {
        memo.resize(m, vector<int>(n, -1));
        return dfs(m-1, n-1);
    }
    int dfs(int i, int j) {
        if (i == 0 && j == 0) return 1;
        if (i < 0 || j < 0) return 0;
        if (memo[i][j] != -1) return memo[i][j];
        memo[i][j] = dfs(i-1, j) + dfs(i, j-1);
        return memo[i][j];
    }
};
