class Solution {
public:
    int res;
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<int> par;
        res = n;
        for (int i = 0; i < n; i++) {
            par.push_back(i);
        }
        vector<int> rank(n, 1);
        for (const auto edge : edges) {
            if (!Union(edge[0], edge[1], par, rank)) return false;
        }
        return res == 1;
    }
    int Find(int x, vector<int> &par) {
        if (par[x] != x) {
            par[x] = Find(par[x], par);
        }
        return par[x];
    }

    bool Union(int e1, int e2, vector<int> &par, vector<int> &rank) {
        int p1 = Find(e1, par);
        int p2 = Find(e2, par);

        if (p1 == p2) return false;
        res--;
        if (rank[p1] < rank[p2]) {
            int temp = p1;
            p1 = p2;
            p2 = temp;
        }
        rank[p1] += rank[p2];
        par[p2] = p1;
        return true;
    }
};
