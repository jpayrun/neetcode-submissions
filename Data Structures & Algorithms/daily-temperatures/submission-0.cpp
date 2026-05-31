class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> t = temperatures;
        vector<int> res (t.size(), 0);
        stack<pair<int, int>> s;
        for (int i = 0; i < t.size(); i++) {
            while (!s.empty() && s.top().second < t[i]) {
                res[s.top().first] = i - s.top().first;
                s.pop();
            }
            s.push({i, t[i]});
        }
        return res;
    }
};
