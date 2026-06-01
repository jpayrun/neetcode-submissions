class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> permute(vector<int>& nums) {
        backtrack(0, nums);
        return res;
    }
    void backtrack(int start, vector<int> &nums) {
        if (start == nums.size()) {
            res.push_back(nums);
            return;
        }
        for (int i = 0; i <= start; i++) {
            swap(nums[i], nums[start]);
            backtrack(start+1, nums);
            swap(nums[i], nums[start]);
        }
    }
    void swap(int &a, int &b) {
        int temp = a;
        a = b;
        b = temp;
    }
};
