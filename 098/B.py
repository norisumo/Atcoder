N = int(input())
S = input()

ans = 0
for i in range(1,N):
    sl = set(S[:i])
    sr = set(S[i:])
    cnt = 0
    for a in sl:
        if a in sr:
            cnt += 1
    ans = max(ans,cnt)
print(ans)



