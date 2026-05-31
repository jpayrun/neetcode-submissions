class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> memo;
        memo.resize(m+1, vector<int>(n+1, -1));
        return helper(0, 0, word1, word2, m, n, memo);
    }
    int helper(int i, int j, string &word1, string &word2, int m, int n, vector<vector<int>> &memo) {
        if (memo[i][j] > -1) return memo[i][j];
        if (i == m) memo[i][j] = n - j;
        else if (j == n) memo[i][j] = m - i;
        else if (word1[i] == word2[j]) memo[i][j] = helper(i+1, j+1, word1, word2, m, n, memo);
        else {
            memo[i][j] = 1 + min(
                helper(i+1, j+1, word1, word2, m, n, memo),
                min(helper(i+1, j, word1, word2, m, n, memo),
                helper(i, j+1, word1, word2, m, n, memo))
            );
        }
        return memo[i][j];
    }
};
