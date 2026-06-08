class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        auto comp = [](const vector<int>& a, const vector<int>& b) {
            return a[2] > b[2];
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(comp)> minHeap (comp);
    
        dist[0][0] = 0;
        minHeap.push({0, 0, 0});

        vector<pair<int, int>> d = {{0,1},{1,0},{-1,0},{0,-1}};

        while (!minHeap.empty()) {
            vector<int> temp = minHeap.top();
            minHeap.pop();
            int r = temp[0], c = temp[1], effort = temp[2];
            
            if (effort > dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return effort;

            for (const auto& [dr, dc] : d) {
                int nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int nextEffort = max(effort, abs(heights[r][c] - heights[nr][nc]));
                    if (nextEffort < dist[nr][nc]) {
                        dist[nr][nc] = nextEffort;
                        minHeap.push({nr, nc, nextEffort});
                    }
                }
            }
        }
        return 0;
    }
};