#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i=0; i < (n); i++)

int main() {
    int N,M;
    cin >> N >> M;
    vector<set<int>> st(N+1);

    rep(i,M) {
        int u,v;
        cin >> u >> v;
        st[u].insert(v);
        st[v].insert(u);
    }

    int ans = 0;
    for(int a = 1; a <= N+1; a++) {
        for(int b=a+1; b <= N+1; b++) {
            if (b <= a) {
                break;
            }
            for(int c=b+1; c <= N+1; c++) {
                if ((b <= a) || (c <= a) || (c <= b)) {
                    break;
                }
                if ((st[a].find(b) != st[a].end()) && (st[b].find(c) != st[b].end()) && (st[c].find(a) != st[c].end())) {
                    ans++;
                }
            }
        }
    }
    cout << ans << endl;
}