#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i,n) for(ll i=0; i<(n); i++)

int H,W,ans;
vector<vector<int>> A;

void dfs(int i, int j, set<int> s) {
    if (s.count(A[i][j])) return;
    if (i == H-1 && j == W-1){
        ans++;
        return;
    }
    s.insert(A[i][j]);
    if(j < W-1) dfs(i, j+1, s);
    if(i < H-1) dfs(i+1, j, s);
}

int main() {
    cin >> H >> W;
    A = vector<vector<int>> (H, vector<int>(W));
    rep(i,H) rep(j,W) cin >> A[i][j];
    dfs(0,0,set<int>());
    cout << ans << endl;
    return 0;
}