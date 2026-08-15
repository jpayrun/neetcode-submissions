class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto comp = [](vector<int> a, vector<int> b) {
            return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1];
        };

        priority_queue <vector<int>, vector<vector<int>>, decltype(comp)> heap(comp);
    

    for (const auto &point : points) {
        heap.push({point[0], point[1]});
        if (heap.size() > k) heap.pop();
    }
    vector<vector<int>> res;
    while (!heap.empty()) {
        res.push_back(heap.top());
        heap.pop();
    }
    return res;
    }
};
