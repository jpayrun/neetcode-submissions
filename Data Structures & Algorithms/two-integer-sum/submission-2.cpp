class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> hash;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int diff = target - num;
            if (hash.count(num) == 1) {
                return {hash[num], i};
            }
            hash[diff] = i;
        }
        return {};
    }
};
