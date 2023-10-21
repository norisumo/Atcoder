from collections import Counter

N = int(input())
A = list(map(int,input().split()))



C = Counter(A)
cnts = list(C.values())
L = len(cnts)

sum_l = [0] * (L+1)
for i in range(L):
    sum_l[i+1] = sum_l[i] + cnts[i]

ans = 0
for j in range(L):
    idx = j + 1
    ans += sum_l[idx-1] * cnts[j] * (sum_l[L] - sum_l[idx])



print(ans)