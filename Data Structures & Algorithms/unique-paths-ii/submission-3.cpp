class Solution {
public:
    vector<vector<int>> memo;
    vector<vector<int>> grid;
    int res = 0;
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        grid = obstacleGrid;
        int m = grid.size();
        int n = grid[0].size();
        if (grid[0][0] == 1) return 0;
        memo.resize(m, vector<int>(n, -1));
        res = helper(0, 0, m, n);

        return res;
    }
    int helper(int i, int j, int m, int n) {
        if (i == m-1 && j == n - 1) return 1;
        if (i == m || j == n) return 0;
        if (grid[i][j] == 1) return 0;
        if (memo[i][j] > -1) return memo[i][j];
        memo[i][j] = helper(i+1, j, m, n) + helper(i, j+1, m, n);
        return memo[i][j];
    }
};