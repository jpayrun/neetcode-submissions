class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue <int> heapMax;
        for (auto &num : nums) {
            heapMax.push(-num);
            if (heapMax.size() > k) {
                heapMax.pop();
            }
        }
        /*
        while (heapMax.size() > 1) {
            heapMax.pop();
        }*/
        return -heapMax.top();
    }
};
