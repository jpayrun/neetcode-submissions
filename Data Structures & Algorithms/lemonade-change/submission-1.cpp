class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int f = 0;
        int t = 0;
        for (const int bill : bills) {
            if (bill == 20) {
                if (t>=1 && f>=1) {
                    f--;
                    t--;
                }
                else if (f >= 3) f-=3;
                else return false;
            }
            if (bill == 10) {
                if (f >= 1) {
                    f-=1;
                    t++;
                }
                else return false;
            } 
            if (bill == 5) f++;
        }
        return true;
    }
};