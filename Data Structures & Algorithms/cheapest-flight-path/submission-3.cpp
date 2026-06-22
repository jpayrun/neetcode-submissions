class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        unordered_map <int, vector<pair<int, int>>> graph;
        for (const auto &flight : flights) {
            graph[flight[0]].push_back({flight[1], flight[2]});
        }
        auto comp = [](vector<int> a, vector<int> b) {
            return a[1] > b[1];
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(comp)> heap(comp);

        heap.push({src, 0, 0});

        unordered_map <int, int> dist;

        while(!heap.empty()) {
            vector<int> tmp = heap.top();
            heap.pop();
            int s = tmp[0];
            int c = tmp[1];
            int st = tmp[2];
            
            if (s == dst) return c;
            if (st > k) continue;
            if (dist.count(s) == 1 && dist[s] <= st) continue;
            dist[s] = st;

            for (const auto [dst, cost] : graph[s]) {
                heap.push({dst, c + cost, st+1});
            }
        }
        return -1;
    }
};
