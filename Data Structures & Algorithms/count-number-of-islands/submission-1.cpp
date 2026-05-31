class Solution {
public:
    int res = 0;
    int directions[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    dfs(i, j, m, n, grid);
                }
            }
        }
        return res;
    }
    void dfs(int i, int j, int m, int n, vector<vector<char>> &grid) {
        grid[i][j] = '0';
        for (const auto [dr, dc] : directions) {
            int row = i + dr;
            int col = j + dc;
            if (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] == '1') {
                dfs(row, col, m, n, grid);
            }
        }
    }
};
