#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<string> A(N);
    for(int i=0; i<N; i++) cin >> A[i];

    bool ans = true;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (i == j) {
                continue;
            }
            if ((A[i][j] == 'W') && (A[j][i] == 'L')){
                continue;
            }  else if  ((A[i][j] == 'L') && (A[j][i] == 'W')){
                continue;
            } else if  ((A[i][j] == 'D') && (A[j][i] == 'D')){
                continue;
            }
            ans = false;
            break;
        }
    }
    if(ans){
        cout << "correct" << endl;
    } else {
        cout << "incorrect" << endl;
    }
}