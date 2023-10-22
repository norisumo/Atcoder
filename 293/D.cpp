#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

#define rep(i,n) for(ll i=0; i<(n); i++)

int main() {
    int N,M;
    cin >> N >> M;
    dsu uf(N);
    int ans_c = 0;
    int ans_s = 0;
    rep(i,M) {
        int A,C;
        char B,D;
        cin >> A >> B >> C >> D;
        A--; C--;
        if (uf.same(A,C)) {
            ans_c++;
        } else {
            uf.merge(A,C);
        }
    }
    ans_s = N - M;
    cout << ans_c << " " << ans_s << endl;

    return 0;
}