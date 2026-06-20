class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        bt(1, path, n, k);
        return res;
    }
    void bt(int i, vector<int> &path, int n, int k) {
        if (path.size() == k) {
            res.push_back(path);
            return;
        }
        if (i > n) return;
        path.push_back(i);
        bt(i+1, path, n, k);
        path.pop_back();
        bt(i+1, path, n, k);
    }
};