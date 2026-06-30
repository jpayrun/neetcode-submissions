class Solution {
public:
    map <vector<int>, int> memo;
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        vector<int> dp(n, 0);

        for (int l = n - 1; l >= 0; l--) {
            for (int r = l; r < n; r ++) {
                bool even = (r - l) % 2 == 0;

                int left = even ? piles[l] : 0;
                int right = even ? piles[r] : 0;

                if (l == r) {
                    dp[r] = left;
                } else {
                    dp[r] = max(dp[r] + left, dp[r-1] + right);
                }
            }
        }
        int total = accumulate(piles.begin(), piles.end(), 0);
        int aliceScore = dp[n-1];
        return aliceScore > (total - aliceScore);
    }
};