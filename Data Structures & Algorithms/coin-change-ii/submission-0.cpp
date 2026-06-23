class Solution {
public:
    vector<vector<int>> memo;
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> temp(coins.size() + 1, vector<int>(amount + 1, -1));
        //memo.resize(amount+1, -1);
        memo = temp;
        return helper(0, amount, coins);
    }
    int helper(int i, int amount, vector<int> &coins) {
        if (amount == 0) return 1;
        if (i == coins.size()) return 0;
        if (amount < 0) return 0;
        if (memo[i][amount] >= 0) return memo[i][amount];
        int take = helper(i, amount - coins[i], coins);
        int skip = helper(i+1, amount, coins);
        memo[i][amount] = take + skip;
        return memo[i][amount];
    }
};
