class Solution {
public:
    int res = 0;
    unordered_set<int> pos;
    unordered_set<int> neg;
    unordered_set<int> col;
    int rows;
    int totalNQueens(int n) {
        rows = n;
        bt(0);
        return res;
    }
    void bt(int n) {
        if (n == rows) res++;
        for (int i = 0; i < rows; i++) {
            int p = n + i;
            int e = n - i;
            if (col.count(i) == 1 || pos.count(p) == 1 || neg.count(e) == 1) {
                continue;
            }

            col.insert(i);
            pos.insert(p);
            neg.insert(e);
            bt(n+1);
            col.erase(i);
            pos.erase(p);
            neg.erase(e);
        }
    }
};