class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> arr(amount+1, amount + 1);
        arr[0] = 0;
        for (int i = 0; i < amount +1; i++) {
            for (const auto coin : coins) {
                if (i - coin >= 0) {
                    arr[i] = min(1 + arr[i - coin], arr[i]);
                }
            }
        }
        return arr[amount] > amount ? -1 : arr[amount];
    }
};
