from collections import defaultdict

d = defaultdict(list)

N = int(input())
for i in range(N):
    s,t = input().split()
    i_t = int(t)
    if not s in d:
        d[s] = [i_t,i+1]

ans_score = 0
ans = N
for s,vl in d.items():
    t,n = vl[0],vl[1]
    if ans_score < t:
        ans = n
        ans_score = t
    elif ans_score == t:
        if ans > n:
            ans = n
print(ans)
