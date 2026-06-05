class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int fresh = 0;
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) fresh++;
                if (grid[i][j] == 2) q.push({i, j});
            }
        }
        int r, c, row, col;
        int res = 0;
        vector<pair<int, int>> d = {{0,1},{1,0},{0,-1},{-1,0}};
        while (!q.empty() && fresh > 0) {
            res+=1;
            int s = q.size();
            for (int i = 0; i < s; i++) {
                pair<int, int> curr = q.front();
                r = curr.first; c = curr.second;
                q.pop();
                for (const auto& [dr, dc] : d) {
                    row = dr + r;
                    col = dc + c;
                    if (row >= 0 && col >= 0 && row < m && col < n && grid[row][col] == 1) {
                        fresh--;
                        grid[row][col] = 2;
                        q.push({row, col});
                    }
                }
            }
        
        }
        return fresh == 0 ? res : -1;
    }    
};

