class Solution {
public:
    int m;
    int n;
    vector<pair<int, int>> d = {{0, 1}, {1,0}, {-1,0}, {0,-1}};
    void solve(vector<vector<char>>& board) {
        m = board.size();
        n = board[0].size();

        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                dfs(i, 0, board);
            }
            if (board[i][n-1] == 'O') {
                dfs(i, n-1, board);
            }
        }

        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') {
                dfs(0, j, board);
            }
            if (board[m-1][j] == 'O') {
                dfs(m-1, j, board);
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == '#') board[i][j] = 'O';
            }
        }
    }
    void dfs(int i, int j, vector<vector<char>> &board) {
        if (i < 0 || j < 0 || i == m || j == n) return;
        if (board[i][j] != 'O') return;
        board[i][j] = '#';
        for (const auto [dr, dc] : d) {
            int row = i + dr;
            int col = j + dc;
            dfs(row, col, board);
        }
    }

};