from collections import Counter
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = Counter(A)
ans = "Yes"
for i in range(M):
    b = B[i]
    if b in C:
        if C[b] == 0:
            ans = "No"
            break
        C[b] -= 1
        continue
    else:
        ans = "No"
        break
print(ans)
