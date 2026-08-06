class Solution {
public:
    int brightestPosition(vector<vector<int>>& lights) {
        map<int, int> diff;

        for (auto &l : lights) {
            int start = l[0] - l[1];
            int end = l[0] + l[1];

            diff[start]++;
            diff[end+1]--;
        }
        int maxBright = 0;
        int cur = 0;
        int res = INT_MIN;

        for (auto &[key, val] : diff) {
            cur+=val;
            if (cur > maxBright) {
                maxBright = cur;
                res = key;
            }
        }
        return res;
    }
};
