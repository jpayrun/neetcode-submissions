class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res (n, 0);
        stack<pair<int, int>> s;
        for (int i = 0; i < n; i++) {
            while (!s.empty() && s.top().second < temperatures[i]) {
                int index = s.top().first;
                res[index] = i - index;
                s.pop();
            }
            s.push({i, temperatures[i]});
        }
        return res;
    }
};
