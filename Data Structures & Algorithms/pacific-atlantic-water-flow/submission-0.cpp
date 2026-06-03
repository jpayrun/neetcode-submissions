class Solution {
public:
    vector<pair<int, int>> directions = {{0,1},{1,0},{-1,0},{0,-1}};
    vector<vector<string>> grid;
    vector<vector<int>> res;
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int ROWS = heights.size();
        int COLS = heights[0].size();
        
        grid.assign(ROWS, vector<string>(COLS, ""));
        res.clear();
        // pacific
        for (int i = 0; i < COLS; i++) {
            dfs(0, i, heights[0][i], "p", heights);
        }
        for (int i = 0; i < ROWS; i++) {
            dfs(i, 0, heights[i][0], "p", heights);
        }
        // atlantic
        for (int i = 0; i < ROWS; i++) {

            dfs(i, COLS-1, heights[i][COLS-1],  "a", heights);
        }
        // atlantic
        for (int i = 0; i < COLS; i++) {
            dfs(ROWS-1, i, heights[ROWS-1][i],  "a", heights);
        }
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j].find("p") != string::npos && grid[i][j].find("a") != string::npos) res.push_back({i, j});
            }
        }
        return res;
    }
    void dfs(int i, int j, int val, string c, vector<vector<int>> &heights) {
        if (i < 0 || i >= heights.size() || j < 0 || j >= heights[0].size()) return;
        if (grid[i][j].find(c) != string::npos) return;
        if (heights[i][j] < val) return;
        
        grid[i][j] += c;
        
        for (const auto [dr, dc] : directions) {
            int row = dr + i;
            int col = dc + j;
            dfs(row, col, heights[i][j], c, heights);
        }

    }
};