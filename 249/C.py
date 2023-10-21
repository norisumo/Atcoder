from collections import defaultdict

N,K = map(int,input().split())
S = []
for i in range(N):
    S.append(input())
ans = 0
n2 = 1 << N
for t in range(n2):
    d = defaultdict()
    for i in range(N):
        if t & (0x01 << i) != 0x00:
            for s in S[i]:
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1
    cnt = 0
    for k,v in d.items():
        if v == K:
            cnt += 1
    ans = max(ans,cnt)

print(ans)


