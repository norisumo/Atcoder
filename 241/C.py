N = int(input())
S = []
for i in range(N):
    S.append(input())

di = [0,1,1,-1]
dj = [1,0,1,-1]

for d in range(4):
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(6):
                ni = i + di[d] * k
                nj = j + dj[d] * k
                if not (0 <= ni < N):
                    break
                if not (0 <= nj < N):
                    break
                if S[ni][nj] == '#':
                    cnt += 1
            if cnt >= 4:
                print("Yes")
                exit()


print("No")