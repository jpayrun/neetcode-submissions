class Solution {
public:
    bool isPalindrome(int x) {
        vector<int> d;
        if (x < 0) return false;
        while (x > 0) {
            d.push_back(x % 10);
            x/=10;
        }
        int l = 0;
        int r = d.size() - 1;
        while (l < r) {
            if (d[l] != d[r]) return false;
            l+=1;
            r-=1;
        }
        return true;
    }
};