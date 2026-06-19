class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int profit = 0;
        int i = 0;
        while (i < prices.size()) {
            while (i + 1 < n && prices[i+ 1] < prices[i]) {
                i++;
            }
            int r = i + 1;
            while (r + 1 < n && prices[r] < prices[r + 1]) {
                r++;
            }
            if (r < n) profit+=prices[r] - prices[i];
            i = r + 1;
        }
        return profit;
    }
};