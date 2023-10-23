#include <bits/stdc++.h>
#include <string.h>
using namespace std;
using ll = long long;

int main()
{
    ll A;
    string B;
    cin >> A >> B;
    B[1] = B[2];
    B[2] = B[3];
    B[3] = 0x00;

    ll t = static_cast<ll>(stoi(B));
    ll ans = A * t / 100;
    cout << ans << endl;

}