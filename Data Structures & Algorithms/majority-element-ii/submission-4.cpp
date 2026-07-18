class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int num1 = 0, num2 = 0;
        int c1 = 0, c2 = 0;
        for (int num : nums) {
            if (num == num1) c1++;
            else if (num == num2) c2++;
            else if (c1 == 0) {
                num1 = num;
                c1=1;
            }
            else if (c2 == 0) {
                num2 = num;
                c2 = 1;
            } else {
                c1--;
                c2--;
            }
        }
        c1 = 0;
        c2 = 0;
        for (int num : nums) {
            if (num1 == num) c1++;
            else if (num2 == num) c2++;
        }
        vector<int> res;
        if (c1 > (nums.size() / 3)) res.push_back(num1);
        if (c2 > (nums.size() / 3)) res.push_back(num2);
        return res;
    }
};