#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    int tn = (c+b-1) / b;
    int an = (a+d-1) / d;
    if (tn <= an) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}