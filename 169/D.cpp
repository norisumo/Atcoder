#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll N;
    cin >> N;
    vector <pair<ll, int>> fs;
    for(ll i=2; i*i <= N; i++) {
        int x = 0;
        while(N%i == 0) {
            N /= i;
            x++;
        }
        if(x == 0) {
            continue;
        }
        fs.emplace_back(i, x);
    }
    if(N != 1) {
        fs.emplace_back(N, 1);
    }
    int ans = 0;
    for(auto p : fs) {
        int x = p.second;
        int b = 1;
        while(b <= x) {
            ans++;
            x -= b;
            b++;
        }
    }
    cout << ans << endl;
    return 0;
}