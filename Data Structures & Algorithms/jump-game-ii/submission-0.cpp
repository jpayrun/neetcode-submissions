class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> arr(nums.size(), INT_MAX);
        arr[0] = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = nums[i]; j > 0; j--) {
                if (i + j >= n) continue;
                arr[i + j] = min(arr[i] + 1, arr[i + j]); 
            }
        }
        return arr[n-1];
    }
};
