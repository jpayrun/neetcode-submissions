class Solution {
public:
    int res = 0;
    int d[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    vector<vector<char>> mp;
    int m;
    int n;
    int numIslands(vector<vector<char>>& grid) {
        mp = grid;
        m = grid.size();
        n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mp[i][j] == '1') {
                    res++;
                    dfs(i, j);
                }
            }
        }
        return res;
    }
    void dfs(int i, int j) {
        mp[i][j] = '0';
        for (const auto [dr, dc] : d) {
            int row = dr + i;
            int col = dc + j;
            if (row >= 0 && row < m && col >= 0 && col < n && mp[row][col] == '1') {
                dfs(row, col);
            }
        }
    }
};
