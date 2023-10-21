#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i=0; i < (n); i++)

int main() {
    int N;

    cin >> N;

    vector<int> A(5*N);
    rep(i,5*N) cin >> A[i];

    sort(A.begin(), A.end());
    int cnt = 0;
    for(int i=N; i < 4*N; i++) {
        cnt += A[i];
    }
    double ans = (double)cnt / double(3*N);

    cout << ans << endl;
}