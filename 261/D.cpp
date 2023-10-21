#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int N,M;
    cin >> N >> M;
    vector<ll> X(N+1);
    for(int i=1; i<=N; i++) cin >> X[i];
    vector<ll> B(N+1);
    for(int i=0; i<M; i++) {
        int c,y;
        cin >> c >> y;
        B[c] = y;
    }

    vector<vector<ll>> dp(N+1, vector<ll>(N+1));
    for(int i=1; i<=N; i++) {
        for(int j=1; j<=i; j++) {
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + X[i] + B[j]);
            dp[i][0] = max(dp[i][0], dp[i-1][j-1]);
        }
    }

    ll ans = 0;
    for(int i=0; i<=N; i++) {
        for(int j=0; j<=N; j++) {
            ans = max(dp[i][j], ans);
        }
    }
    cout << ans << endl;


}