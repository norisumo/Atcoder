#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i,n) for(ll i=0; i<(n); i++)

int main() {
    int N;
    cin >> N;
    vector<int> memo(N);
    rep(i,N) {
        int now = 0;
        cin >> now;
        if(memo[i] == 0) {
            memo[now-1]++;
        }
    }
    int ansNo = 0;
    vector<int> ans(N);
    rep(i, N) {
        if (memo[i] == 0) {
            ans[ansNo] = i+1;
            ansNo++;
        }
    }
    cout << ansNo << endl;
    rep(i, ansNo) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;

}

