class Solution {
public:
    unordered_map<int, vector<int>> mp;
    unordered_set<int> seen;
    unordered_set<int> visited;
    vector<int> res;
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for (int i = 0; i < prerequisites.size(); i++) {
            int pre = prerequisites[i][1];
            int crs = prerequisites[i][0];
            mp[crs].push_back(pre);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i)) return {};
        }
        return res;
    }
    bool dfs(int crs) {
        if (seen.count(crs)) return false;
        if (visited.count(crs)) return true;
        seen.insert(crs);
        visited.insert(crs);
        for (const auto ncrs : mp[crs]) {
            if (!dfs(ncrs)) return false;
        }
        seen.erase(crs);
        res.push_back(crs);
        return true;
    }
};