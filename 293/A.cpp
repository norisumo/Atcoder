#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    string S;
    cin >> S;
    int len = S.length();
    for(int i=0; i<len; i++){
        int n=2*i;
        int m = 2*i + 1;
        swap(S[n], S[m]);
    }
    cout << S << endl;
    return 0;
}
