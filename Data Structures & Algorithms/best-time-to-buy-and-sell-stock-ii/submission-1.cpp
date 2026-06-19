class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int profit = 0;
        int i = 0;
        while (i < n) {
            if (i + 1 < n && prices[i] < prices[i+1]) {
                profit+=prices[i+1] - prices[i];
            }
            i++;
        }
        return profit;
    }
};