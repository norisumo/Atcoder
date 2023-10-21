#include <bits/stdc++.h>
using namespace std;

int main(){
    int l1,r1,l2,r2;
    cin >> l1 >> r1 >> l2 >> r2;
    int s = 0;
    if (l1 < l2) {
        s = l2;
    } else {
        s = l1;
    }
    int e = 0;
    if (r1 < r2) {
        e = r1;
    } else {
        e = r2;
    }
    int ans = e - s;
    if (r1 < l2 || r2 < l1) {
        ans = 0;
    }
    cout << ans << endl;
}