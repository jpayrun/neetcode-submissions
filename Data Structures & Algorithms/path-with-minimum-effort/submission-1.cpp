class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));

        dist[0][0] = 0;

        auto comp = [](vector<int> a, vector<int> b) {
            return a[2] > b[2];
        };
        priority_queue <vector<int>, vector<vector<int>>, decltype(comp)> minHeap(comp);

        minHeap.push({0,0,0});
        vector<pair<int, int>> d = {{0,1},{1,0},{0,-1},{-1,0}};

        while(!minHeap.empty()) {
            vector<int> temp;
            temp = minHeap.top();
            minHeap.pop();
            int r = temp[0], c = temp[1], e = temp[2];
            
            if (dist[r][c] < e) continue;
            if (r == m-1 && c == n -1) return e;

            for (const auto [dr, dc] : d) {
                int nr = r + dr, nc = c + dc;
                if (nr < 0 || nr == m || nc == n || nc < 0) continue;
                int effort = max(e, abs(heights[nr][nc] - heights[r][c]));
                if (effort < dist[nr][nc]) {
                    dist[nr][nc] = effort;
                    minHeap.push({nr, nc, effort});
                }
            }
        }
        return 1;
    }
};