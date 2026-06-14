class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;
        vector<int> res;
        for (const auto a : asteroids) {
            if (st.empty()) st.push(a);
            else if (st.top() < 0) st.push(a);
            else if (a > 0) st.push(a);
            else {
                bool exploded = false;
                while (!st.empty() && st.top() > 0) {
                    int temp = st.top();
                    if (abs(a) == temp) {
                        st.pop();
                        exploded = true;
                        break;
                    }
                    if (abs(a) > temp) {
                        st.pop();
                        continue;
                    }
                    exploded = true;
                    break;
                }
                if (!exploded) st.push(a);
            }
        }
        while (!st.empty()) {
            int val = st.top();
            st.pop();
            res.push_back(val);
        }
        int l = 0, r = res.size() - 1;
        while (l < r) {
            int temp = res[l];
            res[l] = res[r];
            res[r] = temp;
            l++;
            r--;
        }
        return res;
    }
};