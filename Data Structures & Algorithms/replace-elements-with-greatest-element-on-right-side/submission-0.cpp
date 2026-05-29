class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int top = -1;
        for (int i = arr.size() - 1; i >= 0; i--) {
            int temp = top;
            top = max(arr[i], top);
            arr[i] = temp;
        }
        return arr;
    }
};