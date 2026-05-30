class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map <int, vector<pair<int, int>>> graph;

        for (const auto &time : times) {
            int src = time[0];
            int dest = time[1];
            int t = time[2];

            graph[src].push_back({dest, t});
        }

        priority_queue <
            pair<int, int>,
            vector<pair<int, int>>,
            greater<>> minHeap;

        minHeap.push({0, k});

        unordered_map <int, int> dist;

        while (!minHeap.empty()) {
            pair<int, int> val = minHeap.top();
            minHeap.pop();
            int src = val.second;
            int time = val.first;

            if (dist.count(src) == 1) continue;

            dist[src] = time;

            for (const auto [dest, weight] : graph[src]) {

                if (dist.count(dest) == 0) {
                    minHeap.push({weight + time, dest});
                }
            }
        }

        if (dist.size() != n) {
            return -1;
        }
        int res = 0;
        for (const auto &[key, item] : dist) {
            res = max(res, item);
        }
        return res;
    }
};
