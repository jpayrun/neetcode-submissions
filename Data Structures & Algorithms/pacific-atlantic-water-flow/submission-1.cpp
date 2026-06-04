class Solution {
public:
    int R;
    int C;
    vector<pair<int, int>> d = {{1,0},{0,1},{0,-1},{-1,0}};
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        R = heights.size();
        C = heights[0].size();
        vector<vector<bool>> a;
        vector<vector<bool>> p;
        a.resize(R, vector<bool>(C,false));
        p.resize(R, vector<bool>(C,false));
        vector<vector<int>> res;

        // pacific
        for (int i = 0; i < C; i++) {
            dfs(0, i, 0, heights, p);
        }
        for (int i = 0; i < R; i++) {
            dfs(i, 0, 0, heights, p);
        }
        // atlantic
        for (int i = 0; i < C; i++) {
            dfs(R-1, i, 0, heights, a);
        }
        for (int i = 0; i < R; i++) {
            dfs(i, C-1, 0, heights, a);
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (a[i][j] && p[i][j]) res.push_back({i, j});
            }
        }
        return res;
    }

    void dfs(int i, int j, int val, vector<vector<int>> &h, vector<vector<bool>> &o) {
        if (i < 0 || j < 0 || i == R || j == C) return;
        // already visited
        if (o[i][j]) return;
        if (h[i][j] >= val) o[i][j] = true;
        else return;
        for (const auto [dr, dc] : d) {
            int row = dr + i;
            int col = dc + j;
            dfs(row, col, h[i][j], h, o);
        }
    }
    
};