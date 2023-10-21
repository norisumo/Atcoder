#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
#define rep(i,n) for(int i=0; i<(n); i++)

int main() {
    int N;
    cin >> N;
    string S;
    cin >> S;
    int x=0, y=0;
    set<P> st;
    st.emplace(x,y);
    rep(i,N) {
        if(S[i] == 'R') x++;
        if(S[i] == 'L') x--;
        if(S[i] == 'U') y++;
        if(S[i] == 'D') y--;
        if(st.find({x,y}) != st.end()) {
            cout << "Yes" << endl;
            return 0;
        }
        st.emplace(x,y);
    }
    cout << "No" << endl;

}