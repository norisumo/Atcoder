import bisect
N = int(input())
A = []
for i in range(N):
    t,l,r = map(int, input().split())
    l *= 10
    r *= 10
    if t == 2:
        r -= 5
    elif t == 3:
        l += 5
    elif t == 4:
        l += 5
        r -= 5
    
    A.append([l,r])

A.sort()

ans = 0
for i in range(N):
    l,r = A[i]
    for j in range(i+1,N):
        l2,r2 = A[j]
        if l <= l2 <= r:
            ans += 1
print(ans) 
