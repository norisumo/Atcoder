#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i=0; i < (n); i++)

int main() {
    string s;
    cin >> s;
    rep(i, s.size()) {
        if(isupper(s[i])) cout << i+1 << endl;
    }
    return 0;
}