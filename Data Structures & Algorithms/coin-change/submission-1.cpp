class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> arr(amount + 1, amount + 1);
        arr[0] = 0;
        for (int i = 1; i < arr.size(); i++) {
            for (int c = 0; c < coins.size(); c++) {
                if (coins[c] <= i) {
                    arr[i] = min(arr[i], arr[i - coins[c]] + 1);
                }
            }
        }
        return arr[amount] > amount ? -1 : arr[amount];
    }
};
