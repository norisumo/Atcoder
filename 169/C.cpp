#include <bits/stdc++.h>
#include <string.h>
using namespace std;
using ll = long long;

int main()
{
    ll A;
    double B;
    cin >> A >> B;

    ll t = static_cast<ll>(B*100+0.5);
    ll ans = A * t / 100;
    cout << ans << endl;

}