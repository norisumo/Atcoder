N = int(input())
S = list(map(int, input().split()))
seen = set()
for a in range(1,400):
    for b in range(1,400):
        s = 4 * a * b + 3 * a + 3 * b
        if s > 1000:
            break
        seen.add(s)
ans = 0
for  i in range(N):
    t = S[i]
    if not(t in seen):
        ans += 1




print(ans)