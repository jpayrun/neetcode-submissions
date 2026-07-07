class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        unordered_map <int, vector<pair<int, int>>> graph;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                int dist = abs(x1 - x2) + abs(y1 - y2);
                graph[i].push_back({dist, j});
                graph[j].push_back({dist, i});
            }
        }
        unordered_set<int> visit;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        heap.push({0, 0});
        int res = 0;
        while (visit.size() < n) {
            auto cur = heap.top();
            heap.pop();
            int c = cur.first;
            int i = cur.second;
            if (visit.count(i)) continue;
            visit.insert(i);
            res+=c;
            for (const auto [w, j] : graph[i]) {
                if (!visit.count(j)) heap.push({w, j});
            }
        }
        return res;
    }
};
