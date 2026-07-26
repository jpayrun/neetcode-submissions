class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        while (l < r) {
            int m = l + (r - l) / 2;
            int tot = 0;
            for (const auto &pile : piles) {
                tot+=ceil((1.0 * pile) / m);
            }
            if (tot > h) l = m + 1;
            else r = m;
        }
        return l;
    }
};
