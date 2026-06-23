class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> res;
        for (int i = 0; i <= n; i++) {
            int b = i;
            int val = 0;
            while (b > 0) {
                val += b & 1;
                b = b >> 1;
            }
            res.push_back(val);
        }
        return res;
    }
};
