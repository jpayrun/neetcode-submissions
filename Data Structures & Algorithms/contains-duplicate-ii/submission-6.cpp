class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
         int l = 0;
         unordered_set<int> s;
         for (int r = 0; r < nums.size(); r++) {
            if (r - l > k) {
                s.erase(nums[l]);
                l++;
            }
            if (s.count(nums[r]) == 1) return true;
            s.insert(nums[r]);
         }
         return false;
    }
};