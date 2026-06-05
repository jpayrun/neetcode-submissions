class Solution {
public:
    unordered_map <int, vector<int>> graph;
    unordered_set <int> taken;
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (const auto c : prerequisites) {
            graph[c[0]].push_back(c[1]);
        }

        for (const auto [key, value] : graph) {
            if (!dfs(key)) return false;
        }
        return true;
    }
    bool dfs(int course) {
        if (taken.count(course)) return false;
        if (graph[course].empty()) return true;
        taken.insert(course);
        for (const auto pre : graph[course]) {
            if (!dfs(pre)) return false;
        }
        taken.erase(course);
        graph[course].clear();
        return true;
    }
};
