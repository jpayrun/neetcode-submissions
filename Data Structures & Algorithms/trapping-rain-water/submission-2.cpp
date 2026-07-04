class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = height.size() - 1, l_max = height[l], r_max = height[r];
        int res = 0;
        while (l < r) {
            if (l_max <= r_max) {
                res+=max(0, l_max - height[l]);
                l++;
                l_max = max(l_max, height[l]);
            } else {
                res+=max(0, r_max-height[r]);
                r--;
                r_max = max(r_max, height[r]);
            }
        }
        return res;
    }
};
