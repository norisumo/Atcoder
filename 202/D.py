A,B,K = map(int, input().split())
ans = ""

c = [[0] * 61 for i in range(61)]
c[0][0] = 1
for i in range(60):
    for j in range(i+1):
        c[i+1][j] += c[i][j]
        c[i+1][j+1] += c[i][j]

while (A+B > 0):
    x = 0
    if A >= 1:
        x = c[A+B-1][A-1]
    if K <= x:
        ans += "a"
        A -= 1
    else:
        ans += "b"
        B -= 1
        K -= x

print(ans)
