class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        deque<pair<int, int>> q;
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) q.push_back({i, j});
            }
        }
        vector<pair<int, int>> d = {{0,1},{1,0},{-1,0},{0,-1}};
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop_front();
            for (const auto [dr, dc] : d) {
                int row = r + dr;
                int col = c + dc;
                if (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] == INT_MAX) {
                    grid[row][col] = grid[r][c] + 1;
                    q.push_back({row, col});
                }
            }
        }
    }
};
