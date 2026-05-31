class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<int> rank (n, 1);
        vector<int> par;
        for (int i = 0; i < n; i++) {
            par.push_back(i);
        }

        for (const auto &edge : edges) {
            if (!Union(edge[0], edge[1], par, rank)) {
                return vector<int>({edge[0], edge[1]});
            }
        }
        return {};
    }
private:
    int Find(int n, vector<int> &par) {
        if (n != par[n]) {
            par[n] = Find(par[n], par);
        }
        return par[n];
    }

    bool Union(int n1, int n2, vector<int> &par, vector<int> &rank) {
        int p1 = Find(n1, par);
        int p2 = Find(n2, par);

        if (p1 == p2) return false;

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
