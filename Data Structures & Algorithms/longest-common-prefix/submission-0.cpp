class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res;
        int i = 0;
        while (i >= 0) {
            char c;
            if (strs[0].size() == i) return res;
            else c = strs[0][i];
            for (const auto &s : strs) {
                if (i == s.size()) return res;
                if (c != s[i]) return res;
            }
            res+=c;
            i++;
        }
        return res;
    }
};