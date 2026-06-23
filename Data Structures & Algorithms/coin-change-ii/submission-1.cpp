class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> memo(coins.size() + 1, vector<int>(amount +1, -1));
        return helper(0, amount, coins, memo);
    }
    int helper(int i, int amount, vector<int> &coins, vector<vector<int>> &memo) {
        if (i == coins.size()) return 0;
        if (amount < 0) return 0;
        if (amount == 0) return 1;
        if (memo[i][amount] >= 0) return memo[i][amount];
        int take = helper(i, amount - coins[i], coins, memo);
        int skip = helper(i+1, amount, coins, memo);
        memo[i][amount] = take + skip;
        return memo[i][amount];
    }
    
};
