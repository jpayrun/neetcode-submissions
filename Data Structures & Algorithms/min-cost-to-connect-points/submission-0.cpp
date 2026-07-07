class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        unordered_map<int, vector<pair<int, int>>> graph;
        for (int i = 0; i < points.size(); i++) {
            for (int j = i + 1; j < points.size(); j++) {
                int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                graph[i].push_back({dist, j});
                graph[j].push_back({dist, i});
            }
        }

        int res = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;

        heap.push({0, 0});

        unordered_set<int> visit;

        while (visit.size() < points.size()) {
            auto curr = heap.top();
            heap.pop();
            int c = curr.first;
            int i = curr.second;
            if (visit.count(i)) continue;
            visit.insert(i);
            res+=c;
            for (const auto &nei : graph[i]) {
                if (!visit.count(nei.second)) heap.push({nei.first, nei.second});
            }
        }
        return res;
    }
};
