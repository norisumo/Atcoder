#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); ++i)
typedef long long ll;

int main() {
    int N;
    int C;
    cin >> N >> C;
    /*
    * bit演算においては各bitごとに独立しているという特性を活用する。
    * Vector dでd[0]を全bitが0のセット(=0)、d[1]を全bitが1のセット(=~0)とし、
    * 各操作の度にそれぞれの合成関数を作成していく。
    * 最後にCの0のbitの部分はd[0]の値を、1のbitの部分はd[1]の値を採用する。(C = (C & d[1]) | (~C&d[0]);)の部分
    */
    vector<int> d(2);
    d[1] = ~0;
    rep(i,N) {
        int t,a;
        cin >> t >> a;
        rep(j,2) {
            if(t == 1) d[j] &= a;
            if(t == 2) d[j] |= a;
            if(t == 3) d[j] ^= a;
        }
        C = (C & d[1]) | (~C & d[0]);
        cout << C << endl;
    }
}