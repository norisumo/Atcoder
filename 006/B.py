
n = int(input())

M = 10**6+1
mod = 10007
INF = 1 << 60
triList = [INF] * (M)
triList[0] = 0
triList[1] = 0
triList[2] = 1
idx = 3
while idx < n:
    triList[idx] = ((triList[idx-3] + triList[idx-2]) % mod + triList[idx-1]) % mod
    idx += 1

ans = triList[n-1]
print(ans)
