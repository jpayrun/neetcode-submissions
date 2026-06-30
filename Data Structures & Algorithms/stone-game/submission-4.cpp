class Solution {
public:
    map <vector<int>, int> memo;
    bool stoneGame(vector<int>& piles) {
        int res = dfs(0, piles.size() - 1, piles);
        int tot = accumulate(piles.begin(), piles.end(), 0);
        return res > tot / 2;
    }
    int dfs(int l, int r, vector<int> &piles) {
        if (l > r) return 0;
        if (memo.count({l, r}) == 1) return memo[{l, l}];
        if ((r - l) % 2 == 0) {
            int left = piles[l] + dfs(l+1, r, piles);
            int right = piles[r] + dfs(l, r-1, piles);
            memo[{l, r}] = max(left, right);
        }
        else {
            memo[{l, r}] = max(dfs(l + 1, r, piles), dfs(l, r-1, piles));
        }
        return memo[{l, r}];
    }
};