N,M = map(int, input().split())
t = []
for i in range(N):
    t.append(list(map(int, input().split())))

n = t[0][0]
j = n % 7 
if j == 0:
    j = 7
i = (n - j) // 7 + 1
sj = j
for n in range(N):
    j = sj
    for m in range(M):
        a = (i-1) * 7 + j
        if t[n][m] != a:
            exit(print("No"))
        j = (j+1) % 7
        if j == 0:
            j = 7
    i += 1


print("Yes")