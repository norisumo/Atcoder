#include <bits/stdc++.h>
#include <string.h>

using namespace std;

#define rep(i,n) for(int i=0; i<(n); i++)

int main()
{
    int H,W;
    cin >> H >> W;
    vector<string> s(H, string(W, '.'));
    rep(i,H){
        rep(j,W){
            int a = 0;
            cin >> a;
            if(a == 0) {
                continue;
            }
            s[i][j] = 'A' + a - 1;
        }
    }
    rep(i, H){
        cout << s[i] << endl;
    }
}