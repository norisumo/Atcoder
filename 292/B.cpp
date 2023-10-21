#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0; i<(n); i++)
#define INF 1000000000+1

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<int> S(N+1);
    rep(i,Q){
        int c,x;
        cin >> c >> x;
        if (c == 1) {
            S[x] += 1;
        } else if(c == 2) {
            S[x] += 2;
        } else {
            if (S[x] >= 2){
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }

    return 0;
}