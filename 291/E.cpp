#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i=0; i<(n); i++)

int main() {
    int n,m;
    cin >> n >> m;
    vector<vector<int>> to(n);
    vector<int> deg(n);
    rep(i,m) {
        int a,b;
        cin >> a >> b;
        --a;
        --b;
        to[b].push_back(a);
        deg[a]++;
    }

    queue<int> q;
    rep(i,n) {
        if(deg[i] == 0) q.push(i);
    }
    vector<int> A(n);
    int na = n;
    while(q.size()) {
        if(q.size() > 1) {
            cout << "No" << endl;
            return 0;
        }
        int v = q.front();
        q.pop();
        A[v] = na;
        na --;
        for(int u:to[v]){
            deg[u]--;
            if(deg[u] == 0) {
                q.push(u);
            }
        }
    }
    cout << "Yes" << endl;
    rep(i,n) cout << A[i] << ' ';
    cout << endl;
}