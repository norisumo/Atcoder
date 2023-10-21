#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i,n) for(ll i=0; i<(n); i++)
#define INF 1000000000+1

int main() {
    string S;
    cin >> S;
    rep(i,S.size()) {
        S[i] += 'A' - 'a';
    }
    cout << S << endl;
    return 0;
}