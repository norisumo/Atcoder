N = int(input())
L = list(map(int,input().split()))
en = 10 ** 3
d = [0] * (en + 1)

for i in range(N):
    l = L[i]
    d[l] += 1

s = [0] * (en + 1)

for i in range(1, en+1):
    s[i] = s[i-1] + d[i]

ans = 0
for i in range(N):
    l = L[i]
    ml = l // 2