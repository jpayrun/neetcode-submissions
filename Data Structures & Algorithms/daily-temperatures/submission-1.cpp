class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res (temperatures.size(), 0);
        stack<pair<int, int>> s;
        for (int i = 0; i < temperatures.size(); i++) {
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
