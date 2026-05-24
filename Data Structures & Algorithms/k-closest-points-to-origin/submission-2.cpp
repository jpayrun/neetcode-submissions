class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto comp = [](const vector<int> &a, const vector<int> &b) {
            return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1];
        };

    priority_queue <vector<int>, vector<vector<int>>, decltype(comp)> maxHeap(comp);

    for (const auto &point : points) {
        maxHeap.push({point[0], point[1]});

        if (maxHeap.size() > k) maxHeap.pop();
    }

    vector<vector<int>> result;

    while (!maxHeap.empty()) {
        result.push_back(maxHeap.top());
        maxHeap.pop();
    }
    return result;
    }
};