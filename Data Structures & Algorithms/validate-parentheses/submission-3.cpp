class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (const auto c : s) {
            if (c == '(') st.push(c);
            else if (c == '[') st.push(c);
            else if (c == '{') st.push(c);
            else if (st.empty()) return false;
            else if (c == ')') {
                if (st.top() != '(') return false;
                else st.pop();
            }
            else if (c == ']') {
                if (st.top() != '[') return false;
                else st.pop();
            }
            else if (c == '}') {
                if (st.top() != '{') return false;
                else st.pop();
            }
        }

        return st.empty();
    }
};
