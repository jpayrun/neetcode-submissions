class Solution {
public:
    vector<string> res;
    vector<string> generateParenthesis(int n) {
        string path;
        bt(n, n, 0, path);
        return res;
    }
    void bt(int left, int right, int count, string &path) {
        if (left == 0 && right == 0) {
            res.push_back(path);
            return;
        }
        if (left > 0) {
            path.push_back('(');
            bt(left-1, right, count+1, path);
            path.pop_back();
        }
        if (right > 0 && count > 0) {
            path.push_back(')');
            bt(left, right -1, count -1, path);
            path.pop_back();
        }
    }
};
