class KthLargest {
public:
    priority_queue <int, vector<int>, greater<int>> minHeap;
    int n;
    KthLargest(int k, vector<int>& nums) {
        this->n = k;
        for (const auto &num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        if (minHeap.size() > n) minHeap.pop();
        return minHeap.top();
    }
};
