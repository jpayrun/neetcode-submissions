class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int l = 0;
        int r = 0;
        for (const auto weight : weights) {
            l = max(l, weight);
            r += weight;
        }

        while (l < r) {
            int m = l + (r - l) / 2;
            if (fillBoat(m, weights, days)) r = m;
            else l = m+1;
        }
        return l;
    }
    bool fillBoat(int val, vector<int>& weights, int days) {
        int res = 0;
        int tot = 0;
        for (const auto weight : weights) {
            if (weight > val) return false;
            if (tot + weight == val) {
                tot = 0;
                res++;
            }
            else if (tot + weight > val) {
                tot = weight;
                res++;
            } else tot+=weight;
        }
        if (tot > 0) res++;
        return res <= days;
    }
};