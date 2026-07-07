class Solution {
public:
    int trap(vector<int>& height) {
    int l = 0, r = height.size() - 1, l_max = 0, r_max = 0, res = 0;
    while (l < r) {
        l_max = max(l_max, height[l]);
        r_max = max(r_max, height[r]);
        if (l_max < r_max) {
            res += l_max - height[l];
            l++;
        } else {
            res += r_max - height[r];
            r--;
        }
    }

    return res;
    }
};