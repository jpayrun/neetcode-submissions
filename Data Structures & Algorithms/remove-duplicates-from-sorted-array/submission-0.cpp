class Solution {
public:
    unordered_set<int> mp;
    int removeDuplicates(vector<int>& nums) {
        vector<int> temp;
        for (const auto num : nums) {
            if (mp.count(num) == 1) continue;
            mp.insert(num);
            temp.push_back(num);
        }
        nums = temp;
        return mp.size();
    }
};