#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i=0; i < (n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> a(N+1);
    rep(i, N) {
        cin >> a[i+1];
    }

    ll n = 0;
    for(int i=1; i<=N; i++) {
        if (i == a[i]) {
            n++;
        }
    }
    ll ans = 0;
    for(int i=1; i<=N; i++) {
        int t = a[i];
        if((i != t) && (a[t] == i)) {
            ans++;
        }
    }
    ans /= 2;
    if (n >= 2) {
        ans += n*(n-1) / 2;
    }   
    cout << ans << endl;

}