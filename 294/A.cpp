#include <bits/stdc++.h>
//#include <atcoder/all>
using namespace std;
//using namespace atcoder;
using ll = long long;

#define rep(i,n) for(ll i=0; i<(n); i++)

int main() {
    int N;
    cin >> N;
    vector <int> A(N);
    rep(i,N) {
        cin >> A[i];
    }
    for(int a:A) {
        if (a%2 == 0) {
            cout << a << " ";
        }
    }
    cout << endl;
}