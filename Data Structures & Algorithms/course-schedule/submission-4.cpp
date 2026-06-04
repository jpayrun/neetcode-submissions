class Solution {
public:
    unordered_map <int, vector<int>> graph;
    unordered_set <int> taken;
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        for (const auto c : prerequisites) {
            int course = c[1];
            int pre = c[0];
            graph[course].push_back(pre);
        }
        for (const auto [course, pre] : graph) {
            if (!dfs(course)) return false;
        }
        return true;
    }
    bool dfs(int course) {
        if (graph[course].empty()) return true;
        taken.insert(course);
        for (const auto pre : graph[course]) {
            if (taken.count(pre) == 1) return false;
            if (!dfs(pre)) return false;
        }
        taken.erase(course);
        graph[course].clear();
        return true;
    }
};
