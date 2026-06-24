class Solution {
public:
    vector<vector<int>> memo;
    int m;
    int n;
    int minPathSum(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        memo.resize(m, vector<int>(n, -1));
        return helper(0, 0, grid);
    }
    int helper(int i, int j, vector<vector<int>> &grid) {
        if (i == m || j == n) return 20001;
        if (i == m - 1 && j == n - 1) return grid[i][j];
        if (memo[i][j] > -1) return memo[i][j];
        int down = helper(i+1, j, grid) + grid[i][j];
        int right = helper(i, j+1, grid) + grid[i][j];
        memo[i][j] = min(down, right);
        return memo[i][j];
    }
};