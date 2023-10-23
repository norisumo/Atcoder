#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    ll ans = 1;
    int N = 0;
    cin >> N;
    const ll MX = pow(10,18);
    for(int i=0; i<N; i++) {
        ll a = 0;
        cin >> a; 
        if (a == 0) {
            ans = 0;
            break;
        }       
        if (MX/ans < a || MX < ans*a) {
            ans = MX + 1;
        } else {
            ans *= a;
        }
    }
    if (MX < ans) {
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }
    
}