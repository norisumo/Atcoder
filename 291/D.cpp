#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
using mint = modint998244353;
#define rep(i,n) for(int i=0; i < (n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> a(N), b(N);
    rep(i,N) cin >> a[i] >> b[i];

    vector<vector<mint>> dp(N, vector<mint>(2));
    dp[0][0] = dp[0][1] = 1;

    for(int i=0; i<N; i++) {
        if (a[i] != a[i-1]) dp[i][0] += dp[i-1][0];
        if (a[i] != b[i-1]) dp[i][0] += dp[i-1][1];
        if (b[i] != a[i-1]) dp[i][1] += dp[i-1][0];
        if (b[i] != b[i-1]) dp[i][1] += dp[i-1][1];
    }

    mint ans = dp[N-1][0] + dp[N-1][1];
    cout << ans.val() << endl;
    return 0;
    
}