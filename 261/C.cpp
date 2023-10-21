#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    map<string, int> mp;

    for(int i=0; i<N; i++) {
        string s;
        cin >> s;
        if (mp.find(s) == mp.end()) {
            mp[s] = 1;
            cout << s << endl;
        } else {
            int n = mp[s];
            cout << s << "(" << n << ")" << endl;
            n += 1;
            mp[s] = n;
        }
    }
}