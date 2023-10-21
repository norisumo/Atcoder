#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i,n) for(ll i=0; i<(n); i++)
#define INF 1000000000+1

int main() {
    int N;
    cin >> N;
    vector<int> AB(N+1);
    for(int n= 1; n<N+1; n++) {
        for(int i= 1; i<N+1; i++) {
            if (i*i > n) {
                break;
            }
            int a = i;
            int b = n / i;
            if(n%i == 0) {
                if(a == b) {
                    AB[n] += 1;
                } else {
                    AB[n] += 2;
                }
            }
        }
    }
    ll ans = 0;
    for(int i=1; i < N+1; i++){
        ll ab = AB[i];
        ll cd  = AB[N-i];
        ans += (ab * cd);
        
    }
    cout << ans << endl;

    return 0;
}