class Solution {
public:
    int climbStairs(int n) {
        unordered_map <int, int> hash;
        hash[0] = 0;
        hash[1] = 1;
        hash[2] = 2;
        return helper(n, hash);
    }
    int helper(int n, unordered_map <int, int> &memo) {
            if (memo.count(n) == 1) {
                return memo[n];
            }
            memo[n] = helper(n-1, memo) + helper(n-2, memo);
            return memo[n];
        }
};
