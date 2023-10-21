#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i=0; i < (n); i++)

int main() {
    int Y;
    cin >> Y;

    int t = Y % 4;
    if(t <= 2) {
        cout << Y + (2 - t) << endl;
    } else {
        cout << Y + 3 << endl;
    }

}