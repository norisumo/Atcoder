di = [0,1,0,-1,-1,-1,1,1]
dj = [1,0,-1,0,-1,1,-1,1]

N = int(input())
s = []
for i in range(N):
    s.append(input())

top = 0
for i in range(N):
    for j in range(N):
        top = max(top, int(s[i][j]))

ans = 0
for i in range(N):
    for j in range(N):
        n = int(s[i][j])
        if n != top:
            continue
        for t in range(8):
            now = top
            ni = i
            nj = j
            for k in range(N-1):
                ni = (ni + di[t]) % N
                nj = (nj + dj[t]) % N
                nex = int(s[ni][nj])
                now = now * 10 + nex
            ans = max(ans,now)
                
print(ans)

