class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        while (l < r) {
            int res = numbers[l] + numbers[r];
            if (res == target) return {l + 1, r + 1};
            if (res > target) r--;
            else l++;
        }
        return {};
    }
};
